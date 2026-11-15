

# FibreTrace Data Dictionary

## 1. Introduction

This document explains the fields used in the FibreTrace telemetry dataset. The dataset stores network observations collected during different experiments. These observations will help the Python analysis component identify possible network faults and understand network performance.

Each row represents one network observation from a particular site and experiment.

## 2. Dataset Fields

| Column | Type | Description |
|---|---|---|
| timestamp | datetime | Date and time when the observation was recorded. |
| scenario_id | string | Unique identifier for the experiment or test scenario. |
| site_id | string | Identifies the customer site being monitored, such as SITE-A or SITE-B. |
| data_source | string | Identifies where the observation came from, such as Packet Tracer or a Python-generated dataset. |
| customer_gateway_reachable | integer | Indicates whether the customer gateway is reachable. 1 = reachable, 0 = unavailable. |
| fno_access_reachable | integer | Indicates whether the Fibre Network Operator (FNO) access network is reachable. 1 = reachable, 0 = unavailable. |
| isp_edge_reachable | integer | Indicates whether the ISP edge router is reachable. 1 = reachable, 0 = unavailable. |
| isp_core_reachable | integer | Indicates whether the ISP core network is reachable. 1 = reachable, 0 = unavailable. |
| dns_resolution_ok | integer | Indicates whether DNS resolution completed successfully. 1 = successful, 0 = failed. |
| local_web_reachable | integer | Indicates whether the local web service is reachable. 1 = reachable, 0 = unavailable. |
| global_web_reachable | integer | Indicates whether the global web service is reachable. 1 = reachable, 0 = unavailable. |
| packet_loss_pct | decimal | Percentage of packets that were not successfully received. |
| latency_ms | decimal | Time taken for a network response, measured in milliseconds. |
| jitter_ms | decimal | Variation in network response time, measured in milliseconds. |
| expected_fault_domain | string | The known fault category introduced during an experiment. |
| predicted_fault_domain | string | The fault category identified by the FibreTrace analytical component. |
| diagnosis_explanation | string | Explanation of why the system assigned a particular fault category. |

## 3. Fault Categories

The following categories are used to describe possible network conditions:

| Category | Meaning |
|---|---|
| none | No fault detected; network is operating normally. |
| customer_lan | Problem within the customer's local network. |
| fno_access | Problem within the Fibre Network Operator access network. |
| isp_edge | Problem at the ISP edge router or connection. |
| isp_core | Problem within the ISP core network. |
| dns | DNS service or name-resolution problem. |
| ixp_local | Problem affecting local internet exchange connectivity. |
| transit | Problem affecting upstream internet connectivity. |
| performance | Network performance degradation, such as high latency or packet loss. |
| security_policy | Traffic blocked by a security rule or access control policy. |
| unknown | Available observations are insufficient to identify the fault confidently. |

## 4. Data Values and Missing Information

Reachability and DNS result fields use integer values:

- `1` means the service or network component is reachable or successful.
- `0` means the service or network component is unavailable or unsuccessful.
- `null` means the observation was not collected or is unavailable.

Performance measurements use numeric values. Packet loss is recorded as a percentage, while latency and jitter are recorded in milliseconds.

## 5. Expected and Predicted Faults

The `expected_fault_domain` field stores the known fault category for an experiment. It acts as the reference label when evaluating the analytical component.

The `predicted_fault_domain` field stores the category identified by FibreTrace.

Comparing these two fields makes it possible to measure how accurately the system identifies network faults.

## 6. Dataset Limitations

The current project uses observations from a simulated Packet Tracer environment and Python-based experimental data. It does not collect live operational telemetry from an internet service provider.

Any generated or simulated measurements must be clearly identified as such. They must not be presented as real measurements from a production fibre network.

