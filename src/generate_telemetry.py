
from pathlib import Path
from datetime import datetime, timedelta, timezone

import numpy as np
import pandas as pd


OUTPUT = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "generated"
    / "synthetic_telemetry.csv"
)

SITES = ["SITE_A", "SITE_B"]
SAMPLE_COUNT = 30

SCENARIOS = [
    "normal",
    "customer_lan_failure",
    "fno_access_failure",
    "fno_backhaul_failure",
    "isp_core_failure",
    "ixp_failure",
    "transit_failure",
    "dns_failure",
    "local_web_failure",
    "global_web_failure",
    "congestion",
]

SITE_A_ONLY = {
    "customer_lan_failure",
    "fno_access_failure",
    "fno_backhaul_failure",
    "congestion",
}


def base_state():
    """Return the healthy network state."""

    return {
        "customer_gateway_reachable": 1,
        "fno_access_reachable": 1,
        "isp_edge_reachable": 1,
        "isp_core_reachable": 1,
        "dns_server_reachable": 1,
        "dns_resolution_ok": 1,
        "local_web_ping_ok": 1,
        "local_web_http_ip_ok": 1,
        "local_web_http_name_ok": 1,
        "global_web_ping_ok": 1,
        "global_web_http_ip_ok": 1,
        "global_web_http_name_ok": 1,
    }


def apply_scenario(scenario, site):
    """Apply one controlled fault to the simulated measurements."""

    state = base_state()

    # These failures affect only the first customer.
    if scenario in SITE_A_ONLY and site == "SITE_B":
        return state, "Healthy"

    expected = "Healthy"

    if scenario == "customer_lan_failure":
        state.update({
            "customer_gateway_reachable": 0,
            "fno_access_reachable": 0,
            "isp_edge_reachable": 0,
            "isp_core_reachable": 0,
            "dns_server_reachable": 0,
            "dns_resolution_ok": 0,
            "local_web_ping_ok": 0,
            "local_web_http_ip_ok": 0,
            "local_web_http_name_ok": 0,
            "global_web_ping_ok": 0,
            "global_web_http_ip_ok": 0,
            "global_web_http_name_ok": 0,
        })
        expected = "Customer LAN / CPE"

    elif scenario == "fno_access_failure":
        state.update({
            "fno_access_reachable": 0,
            "isp_edge_reachable": 0,
            "isp_core_reachable": 0,
            "dns_server_reachable": 0,
            "dns_resolution_ok": 0,
            "local_web_ping_ok": 0,
            "local_web_http_ip_ok": 0,
            "local_web_http_name_ok": 0,
            "global_web_ping_ok": 0,
            "global_web_http_ip_ok": 0,
            "global_web_http_name_ok": 0,
        })
        expected = "FNO access"

    elif scenario == "fno_backhaul_failure":
        state.update({
            "isp_edge_reachable": 0,
            "isp_core_reachable": 0,
            "dns_server_reachable": 0,
            "dns_resolution_ok": 0,
            "local_web_ping_ok": 0,
            "local_web_http_ip_ok": 0,
            "local_web_http_name_ok": 0,
            "global_web_ping_ok": 0,
            "global_web_http_ip_ok": 0,
            "global_web_http_name_ok": 0,
        })
        expected = "FNO backhaul / ISP handoff"

    elif scenario == "isp_core_failure":
        state.update({
            "isp_core_reachable": 0,
            "dns_server_reachable": 0,
            "dns_resolution_ok": 0,
            "local_web_ping_ok": 0,
            "local_web_http_ip_ok": 0,
            "local_web_http_name_ok": 0,
            "global_web_ping_ok": 0,
            "global_web_http_ip_ok": 0,
            "global_web_http_name_ok": 0,
        })
        expected = "ISP core"

    elif scenario == "ixp_failure":
        state.update({
            "local_web_ping_ok": 0,
            "local_web_http_ip_ok": 0,
            "local_web_http_name_ok": 0,
        })
        expected = "IXP peering / local content path"

    elif scenario == "transit_failure":
        state.update({
            "global_web_ping_ok": 0,
            "global_web_http_ip_ok": 0,
            "global_web_http_name_ok": 0,
        })
        expected = "Upstream transit"

    elif scenario == "dns_failure":
        state.update({
            "dns_resolution_ok": 0,
            "local_web_http_name_ok": 0,
            "global_web_http_name_ok": 0,
        })
        expected = "DNS"

    elif scenario == "local_web_failure":
        state.update({
            "local_web_http_ip_ok": 0,
            "local_web_http_name_ok": 0,
        })
        expected = "Local web application"

    elif scenario == "global_web_failure":
        state.update({
            "global_web_http_ip_ok": 0,
            "global_web_http_name_ok": 0,
        })
        expected = "Global web application"

    elif scenario == "congestion":
        expected = "Performance degradation"

    return state, expected


def latency_value(rng, reachable, mean, deviation):
    if not reachable:
        return np.nan

    return round(max(0, rng.normal(mean, deviation)), 2)


def main():
    rng = np.random.default_rng(42)

    rows = []
    start = datetime(2026, 1, 1, tzinfo=timezone.utc)

    for scenario_index, scenario in enumerate(SCENARIOS, start=1):

        scenario_id = f"FT-{scenario_index:03d}"

        for site in SITES:

            state, expected = apply_scenario(scenario, site)

            for sample in range(SAMPLE_COUNT):

                congestion = (
                    scenario == "congestion"
                    and site == "SITE_A"
                )

                core_mean = 140 if congestion else 15
                loss = (
                    round(rng.uniform(3.0, 6.0), 2)
                    if congestion
                    else round(rng.uniform(0.0, 1.0), 2)
                )

                jitter = (
                    round(rng.uniform(10, 20), 2)
                    if congestion
                    else round(rng.uniform(0.5, 3), 2)
                )

                timestamp = (
                    start
                    + timedelta(
                        days=scenario_index,
                        minutes=sample
                    )
                )

                row = {
                    "timestamp": timestamp.isoformat(),
                    "data_source": "SYNTHETIC",
                    "scenario_id": scenario_id,
                    "scenario_name": scenario,
                    "site_id": site,
                    "sample_number": sample + 1,
                    "expected_fault_domain": expected,
                    **state,

                    "customer_gateway_latency_ms":
                        latency_value(
                            rng,
                            state["customer_gateway_reachable"],
                            2, 0.5
                        ),

                    "fno_access_latency_ms":
                        latency_value(
                            rng,
                            state["fno_access_reachable"],
                            6, 1
                        ),

                    "isp_edge_latency_ms":
                        latency_value(
                            rng,
                            state["isp_edge_reachable"],
                            12, 2
                        ),

                    "isp_core_latency_ms":
                        latency_value(
                            rng,
                            state["isp_core_reachable"],
                            core_mean, 8 if congestion else 3
                        ),

                    "local_web_latency_ms":
                        latency_value(
                            rng,
                            state["local_web_ping_ok"],
                            25, 4
                        ),

                    "global_web_latency_ms":
                        latency_value(
                            rng,
                            state["global_web_ping_ok"],
                            50, 8
                        ),

                    "packet_loss_pct": loss,
                    "jitter_ms": jitter,
                }

                rows.append(row)

    df = pd.DataFrame(rows)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(OUTPUT, index=False)

    print(f"Dataset created: {OUTPUT}")
    print(f"Total records: {len(df)}")
    print(f"Scenarios: {len(SCENARIOS)}")
    print("Data classification: SYNTHETIC")


if __name__ == "__main__":
    main()
