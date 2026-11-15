

# FibreTrace Real-World Implementation Proposal

## 1. Introduction

FibreTrace is designed as a prototype for identifying and analysing network connectivity problems across different parts of an internet service provider's infrastructure.

Although the current version uses Cisco Packet Tracer and Python, the concept could be developed further into a real network monitoring and fault-diagnosis platform.

This document explains how an organisation could gradually adapt the project for a real operational environment.

## 2. Proposed Implementation Stages

| Stage | Proposed Implementation |
|---|---|
| Current | Develop and test the prototype using Cisco Packet Tracer and Python. |
| Stage 2 | Set up a Linux-based monitoring environment for running network monitoring scripts and services. |
| Stage 3 | Introduce active network probes between authorised monitoring points to test connectivity, latency and packet loss. |
| Stage 4 | Collect network information securely using SNMP and syslog from supported network devices. |
| Stage 5 | Store historical network observations in a database for reporting and analysis. |
| Stage 6 | Introduce advanced analytics and predictive monitoring to identify patterns that may indicate future network faults. |
| Stage 7 | Conduct a controlled pilot with an ISP or enterprise networking team. |

## 3. Linux-Based Monitoring Environment

The next development stage could involve moving the monitoring component from a basic local Python environment to a dedicated Linux server.

Linux would provide a suitable environment for running scheduled monitoring tasks, Python applications and network diagnostic tools.

This would also make it easier to operate the monitoring system continuously.

## 4. Active Network Probes

A real implementation could use authorised monitoring points placed at important locations in the network.

These monitoring points could test:

- Gateway availability.
- Connectivity between network devices.
- DNS resolution.
- Local and external web services.
- Network latency.
- Packet loss.
- Jitter.

By comparing observations from different monitoring points, FibreTrace could help narrow down where a connectivity problem is occurring.

## 5. SNMP and Syslog Integration

FibreTrace could later collect information directly from supported routers, switches and other network equipment.

SNMP could provide information about interface status, traffic levels, device performance and other available network indicators.

Syslog could provide event messages about interface changes, device errors and other network events.

This would give the system more information than basic ping tests alone.

All monitoring would need to be authorised by the organisation responsible for the network.

## 6. Database-Backed Historical Telemetry

A database could be introduced to store network observations over time.

This would allow the system to compare current network conditions with historical behaviour.

It could also support dashboards, reports, trend analysis and investigation of repeated faults.

## 7. Advanced Analytics and Predictive Monitoring

Once enough reliable observations have been collected, FibreTrace could introduce more advanced analytical techniques.

Possible improvements include:

- Identifying unusual network behaviour.
- Detecting repeated connectivity failures.
- Comparing performance across different network sections.
- Classifying possible fault locations.
- Identifying patterns that occur before service degradation.
- Providing explanations for its diagnostic results.

Machine learning could be explored once sufficient representative and correctly labelled data is available.

The system should provide confidence levels and explanations rather than treating every prediction as certain.

## 8. Controlled Pilot Implementation

Before wider deployment, FibreTrace could be tested with an ISP or enterprise networking team in a controlled environment.

The pilot could focus on a limited number of authorised network devices and monitoring points.

The organisation could evaluate:

- Accuracy of fault identification.
- Time required to detect problems.
- False positive warnings.
- Reliability of collected telemetry.
- Usefulness of diagnostic explanations.
- Security and privacy requirements.

Feedback from the pilot would help identify areas requiring improvement before any wider rollout.

## 9. Expected Benefits

A mature FibreTrace implementation could provide several potential benefits:

- Faster identification of possible network fault locations.
- Better visibility across different network sections.
- Easier comparison of network performance over time.
- Improved reporting for technical teams.
- Earlier identification of unusual network behaviour.
- Support for network troubleshooting and maintenance decisions.

These are proposed benefits and would need to be evaluated through real-world testing.

## 10. Conclusion

FibreTrace provides a starting point for developing a network fault-diagnosis and monitoring solution.

The current project demonstrates the concept using a simulated network and Python-based analysis.

With further development, real telemetry integration, security controls and controlled testing, the system could be adapted for evaluation in an ISP or enterprise network environment.

The proposed stages describe a possible future implementation. They do not mean that the current prototype already has production monitoring or predictive capabilities.

