
from pathlib import Path
import math

import pandas as pd
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]

DATA_FILE = (
    ROOT / "data" / "generated" / "synthetic_telemetry.csv"
)

REPORT_DIR = ROOT / "reports"


def check(row, column):
    """Check whether a telemetry indicator is operational."""

    return int(row[column]) == 1


def diagnose(row):
    """
    Apply ordered fault-isolation rules.

    The earliest failed service-chain checkpoint takes priority.
    """

    if not check(row, "customer_gateway_reachable"):
        return "Customer LAN / CPE"

    if not check(row, "fno_access_reachable"):
        return "FNO access"

    if not check(row, "isp_edge_reachable"):
        return "FNO backhaul / ISP handoff"

    if not check(row, "isp_core_reachable"):
        return "ISP core"

    if not check(row, "dns_server_reachable"):
        return "DNS"

    if not check(row, "dns_resolution_ok"):
        return "DNS"

    if not check(row, "local_web_ping_ok"):
        return "IXP peering / local content path"

    if not check(row, "local_web_http_ip_ok"):
        return "Local web application"

    if not check(row, "global_web_ping_ok"):
        return "Upstream transit"

    if not check(row, "global_web_http_ip_ok"):
        return "Global web application"

    packet_loss = float(row["packet_loss_pct"])
    core_latency = float(row["isp_core_latency_ms"])

    if (
        packet_loss >= 2.0
        or (
            math.isfinite(core_latency)
            and core_latency >= 100
        )
    ):
        return "Performance degradation"

    return "Healthy"


def main():

    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Telemetry file not found: {DATA_FILE}. "
            "Run generate_telemetry.py first."
        )

    df = pd.read_csv(DATA_FILE)

    if df.empty:
        raise ValueError("The telemetry dataset is empty.")

    df["predicted_fault_domain"] = df.apply(
        diagnose, axis=1
    )

    # Take the final observation from every scenario/site pair.
    latest = (
        df.sort_values("timestamp")
        .groupby(
            ["scenario_id", "scenario_name", "site_id"],
            as_index=False
        )
        .tail(1)
        .copy()
    )

    results_file = REPORT_DIR / "diagnosis_results.csv"

    latest.to_csv(results_file, index=False)

    # Compare the rule-based result with the generated labels.
    consistency = (
        latest["expected_fault_domain"]
        == latest["predicted_fault_domain"]
    ).mean() * 100

    summary = (
        latest.groupby(
            ["scenario_name", "predicted_fault_domain"]
        )
        .size()
        .reset_index(name="number_of_site_results")
    )

    summary_file = REPORT_DIR / "diagnosis_summary.csv"
    summary.to_csv(summary_file, index=False)

    # Create a latency profile from normal-operation records.
    normal = df[df["scenario_name"] == "normal"]

    latency_columns = [
        "customer_gateway_latency_ms",
        "fno_access_latency_ms",
        "isp_edge_latency_ms",
        "isp_core_latency_ms",
        "local_web_latency_ms",
        "global_web_latency_ms",
    ]

    labels = [
        "Customer GW",
        "FNO Access",
        "ISP Edge",
        "ISP Core",
        "Local Web",
        "Global Web",
    ]

    plt.figure(figsize=(10, 5))

    for site, group in normal.groupby("site_id"):

        mean_latency = group[latency_columns].mean()

        plt.plot(
            labels,
            mean_latency.values,
            marker="o",
            label=site
        )

    plt.title("FibreTrace: Normal Network Latency Profile")
    plt.xlabel("Network Test Point")
    plt.ylabel("Average Latency (ms)")
    plt.xticks(rotation=20)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        REPORT_DIR / "normal_latency_profile.png",
        dpi=160
    )

    plt.close()

    # Create a fault-classification count chart.
    counts = latest["predicted_fault_domain"].value_counts()

    plt.figure(figsize=(10, 5))
    counts.plot(kind="bar")

    plt.title("FibreTrace: Diagnostic Classification Results")
    plt.xlabel("Predicted Fault Domain")
    plt.ylabel("Number of Site Results")
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()

    plt.savefig(
        REPORT_DIR / "fault_classification_results.png",
        dpi=160
    )

    plt.close()

    print("\nFIBRETRACE DIAGNOSTIC REPORT")
    print("=" * 40)

    print(f"Dataset records: {len(df)}")
    print(f"Scenario/site results: {len(latest)}")

    print(
        "Synthetic rule-label consistency: "
        f"{consistency:.2f}%"
    )

    print("\nCLASSIFICATIONS")
    print(summary.to_string(index=False))

    print("\nREPORT FILES")
    print(results_file)
    print(summary_file)
    print(REPORT_DIR / "normal_latency_profile.png")
    print(REPORT_DIR / "fault_classification_results.png")

    print(
        "\nNOTE: Synthetic consistency is not proof of "
        "real-world diagnostic accuracy."
    )


if __name__ == "__main__":
    main()
