# FibreTrace — Executive Summary

## 1. Project Overview

FibreTrace is a network monitoring and fault-diagnosis prototype designed to demonstrate how network problems can be identified across different service-provider domains.

The project uses Cisco Packet Tracer to simulate a multi-provider network and Python to analyse network observations and produce understandable diagnostic results.

The main idea is to go beyond simply reporting that an internet connection is unavailable. FibreTrace should examine different parts of the network and help identify where a problem is most likely occurring.

## 2. Problem Statement

An internet connection depends on several network components working together. These may include the customer's local network, a Fibre Network Operator (FNO), an Internet Service Provider (ISP), an Internet Exchange Point (IXP), an upstream transit provider, DNS and the destination server.

When a customer experiences connectivity problems, it is not always easy to determine which part of the network is responsible.

For example, a website may fail to load because:
- The customer's gateway is unavailable.
- The FNO access connection is experiencing a problem.
- The ISP edge or core is unavailable.
- DNS cannot resolve the website address.
- The local peering or upstream transit path is failing.
- The destination web server is not responding.

FibreTrace aims to make this troubleshooting process more organised by analysing several network indicators instead of relying on one connectivity test.

## 3. Proposed Solution

FibreTrace combines two main components.

**Network simulation**

Cisco Packet Tracer is used to create a simulated network containing two customer sites, separate FNO access domains, a shared ISP, an IXP connection, an upstream transit connection, DNS and web servers.

**Python analytical system**

Python is used to process network observations, analyse connectivity and performance indicators, classify likely fault domains and produce reports and charts.

The system will examine the network service chain and use the earliest meaningful failed test to narrow down the possible location of a fault.

## 4. Network Design

The network contains two independent customer sites.

Site A uses PC-A, SW-A, CPE-A and FNO-A.

Site B uses PC-B, SW-B, CPE-B and FNO-B.

Both sites connect through ISP-EDGE and ISP-CORE. The ISP core provides access to the IXP peer, transit provider and DNS service.

The IXP peer connects to LOCAL-WEB, while the transit router connects to GLOBAL-WEB.

Extended Access Control Lists (ACLs) are used on ISP-EDGE to prevent direct communication between the two customer networks while permitting other traffic according to the configured rules.

## 5. Technologies Used

| Technology | Purpose |
|---|---|
| Cisco Packet Tracer | Network design, simulation and connectivity testing |
| Python 3.12 | Development of the diagnostic system |
| Pandas | Data processing and analysis |
| NumPy | Numerical calculations and synthetic data generation |
| Matplotlib | Graphs and performance visualisations |
| Visual Studio Code | Development environment |
| Git and GitHub | Version control and project hosting |

## 6. Expected Project Outputs

The completed project is expected to produce:

- A working simulated multi-provider network.
- A documented network topology and device inventory.
- A set of repeatable network testing scenarios.
- Evidence of normal and failed network conditions.
- A structured network telemetry dataset.
- A Python diagnostic engine.
- Fault-domain classifications with explanations.
- Performance charts showing relevant network indicators.
- Technical documentation explaining the design and implementation.

## 7. Project Scope

FibreTrace is currently an educational prototype. It is designed to demonstrate network fault isolation using simulated connectivity tests and structured data.

The project does not currently connect to real ISP or FNO infrastructure. It does not collect live production network telemetry or measure actual fibre optical conditions.

Any generated performance measurements must be clearly identified as synthetic rather than real network measurements.

## 8. Project Success Criteria

The project will be considered successful when:

1. The Packet Tracer network matches the documented architecture.
2. Both customer sites can reach the services permitted by the network design.
3. Customer-to-customer traffic is restricted by the ACL policy.
4. Different network faults can be introduced and restored.
5. Python can process the collected observations.
6. The diagnostic engine can identify likely fault domains.
7. The system can produce understandable reports and charts.
8. The project contains sufficient technical documentation and test evidence.

## 9. Conclusion

FibreTrace demonstrates how network simulation and data analysis can be combined to improve the way connectivity problems are investigated.

The project starts with a controlled network environment and a Python-based analytical system, with the possibility of expanding towards more advanced monitoring and diagnostic capabilities in the future.