
import unittest

from src.analyze import diagnose


def healthy_row():

    return {
        "customer_gateway_reachable": 1,
        "fno_access_reachable": 1,
        "isp_edge_reachable": 1,
        "isp_core_reachable": 1,
        "dns_server_reachable": 1,
        "dns_resolution_ok": 1,
        "local_web_ping_ok": 1,
        "local_web_http_ip_ok": 1,
        "global_web_ping_ok": 1,
        "global_web_http_ip_ok": 1,
        "packet_loss_pct": 0.5,
        "isp_core_latency_ms": 15.0,
    }


class FibreTraceDiagnosticTests(unittest.TestCase):

    def test_healthy_network(self):
        row = healthy_row()
        self.assertEqual(diagnose(row), "Healthy")

    def test_customer_lan_failure(self):
        row = healthy_row()
        row["customer_gateway_reachable"] = 0
        self.assertEqual(
            diagnose(row),
            "Customer LAN / CPE"
        )

    def test_fno_access_failure(self):
        row = healthy_row()
        row["fno_access_reachable"] = 0
        self.assertEqual(diagnose(row), "FNO access")

    def test_fno_backhaul_failure(self):
        row = healthy_row()
        row["isp_edge_reachable"] = 0
        self.assertEqual(
            diagnose(row),
            "FNO backhaul / ISP handoff"
        )

    def test_isp_core_failure(self):
        row = healthy_row()
        row["isp_core_reachable"] = 0
        self.assertEqual(diagnose(row), "ISP core")

    def test_dns_failure(self):
        row = healthy_row()
        row["dns_resolution_ok"] = 0
        self.assertEqual(diagnose(row), "DNS")

    def test_transit_failure(self):
        row = healthy_row()
        row["global_web_ping_ok"] = 0
        self.assertEqual(diagnose(row), "Upstream transit")

    def test_congestion(self):
        row = healthy_row()
        row["packet_loss_pct"] = 4.0
        self.assertEqual(
            diagnose(row),
            "Performance degradation"
        )


if __name__ == "__main__":
    unittest.main()
