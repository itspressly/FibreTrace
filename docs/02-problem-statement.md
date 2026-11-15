# FibreTrace — Problem Statement and Requirements

## 1. Introduction

Modern internet connectivity depends on several network components and service providers working together. A customer's connection may pass through a local network, a Fibre Network Operator (FNO), an Internet Service Provider (ISP), an Internet Exchange Point (IXP) or an upstream transit provider before reaching its destination.

When connectivity problems occur, identifying the responsible network domain can be difficult because several different failures may produce similar symptoms.

FibreTrace aims to address this problem by creating a simulated multi-provider network and a Python analytical system that evaluates network observations and identifies likely fault domains.

## 2. Problem Statement

When a customer reports that an internet connection or online service is unavailable, the problem may originate from several different parts of the network.

A basic connectivity test may confirm that a destination is unreachable, but it does not necessarily explain why.

The problem FibreTrace addresses is the difficulty of identifying the earliest failing point in a multi-provider service chain.

The proposed system will analyse multiple indicators, including gateway reachability, FNO access, ISP connectivity, DNS availability, web-server availability, latency, packet loss and jitter.

By combining these observations, the system should provide a more useful explanation of the likely problem.

## 3. Main Objective

To identify likely network fault domains using structured connectivity, performance and service-availability indicators from a simulated multi-provider network.

## 4. Functional Requirements

| ID | Requirement | Description |
|---|---|---|
| FR-01 | Two customer sites | The network must simulate two independent customer sites with separate IP networks. |
| FR-02 | Separate FNO domains | Each customer site must use its own hypothetical FNO access domain. |
| FR-03 | Shared ISP | Both customer sites must connect through a shared simulated ISP. |
| FR-04 | Separate external paths | The ISP must provide separate IXP and upstream transit connectivity paths. |
| FR-05 | Network services | DNS and web services must be accessible under normal network conditions. |
| FR-06 | Fault testing | The network must support controlled failure testing. |
| FR-07 | Data analysis | The Python system must analyse structured network indicators. |
| FR-08 | Fault classification | The diagnostic engine must classify likely network fault domains. |
| FR-09 | Reports and charts | The project must produce understandable diagnostic reports and performance charts. |
| FR-10 | Test evidence | Network tests and analytical results must be documented and stored. |

## 5. Non-Functional Requirements

The project must also meet the following requirements:

### Reproducibility
Experiments should be repeatable. Test procedures, input data and synthetic-data generation settings should be documented.

### Readability
Python code should use understandable variable names, functions and comments.

### Maintainability
The project should have a clear folder structure so that new tests, network domains and analytical features can be added.

### Data Accuracy
Observed Packet Tracer results must be distinguished from synthetic or generated data.

### Security
No real ISP credentials, production passwords or private customer information should be included.

### Privacy
The prototype should not collect unnecessary personal information.

### Extensibility
The system should allow additional customer sites, network indicators and fault categories to be added in future versions.

### Clear Reporting
Diagnostic results should explain what failed, which domain is suspected and what should be checked next.

## 6. Project Scope

### Included in the project

- Two simulated customer networks.
- Two separate hypothetical FNO access domains.
- Shared ISP edge and core.
- IXP and transit connectivity.
- DNS and web services.
- Customer separation using ACLs.
- Controlled network failure scenarios.
- Python-based data analysis.
- Fault classification.
- Performance visualisations.
- Technical documentation.

### Outside the current project scope

- Connecting to real ISP infrastructure.
- Accessing production network devices.
- Collecting live customer traffic.
- Measuring real fibre optical power or attenuation.
- Automatically changing production network configurations.
- Providing guaranteed root-cause identification.

## 7. Main Assumptions

The current design uses the following planned addressing information:

| Component | Planned IP address |
|---|---|
| PC-A | 10.10.10.10 |
| Site A gateway | 10.10.10.1 |
| PC-B | 10.20.20.10 |
| Site B gateway | 10.20.20.1 |
| DNS-SERVER | 10.50.50.53 |
| LOCAL-WEB | 198.51.100.10 |
| GLOBAL-WEB | 203.0.113.10 |

The customer networks use /24 subnet masks.

The web-server addresses belong to ranges reserved for documentation and examples. They are used for the simulation and are not real public production addresses.

Router-to-router addressing and VLAN gateway addresses must be recorded from the actual Packet Tracer configuration.

## 8. Acceptance Criteria

A requirement should only be marked as complete when it has been implemented and tested.

The following status descriptions will be used:

- **Pending:** The feature has not yet been implemented or tested.
- **Configured:** The configuration has been entered but has not passed verification.
- **Pass:** The feature has been tested successfully.
- **Fail:** The test did not produce the expected result.
- **Blocked:** The test could not be completed because of another issue.

The final project should contain evidence supporting its completed requirements.