# FibreTrace

### Multi-Provider Fibre Fault Attribution and Service Assurance Platform

FibreTrace is a networking and data analytics portfolio project that investigates connectivity failures across a simulated telecommunications service chain.

The project combines Cisco Packet Tracer network simulation with Python-based telemetry analysis to explore network performance, investigate faults, and identify possible fault domains.

## Project Objectives

- Simulate multiple customer connectivity environments.
- Represent separate hypothetical Fibre Network Operator (FNO) access domains.
- Model ISP edge and core connectivity.
- Demonstrate Internet Exchange Point (IXP) peering and upstream transit paths.
- Introduce and investigate network failures.
- Analyse network performance indicators.
- Identify likely fault domains using analytical techniques.
- Generate diagnostic outputs to support network troubleshooting.

## Network Architecture

The simulated network represents two customer sites connected through separate FNO access domains to a shared Internet Service Provider (ISP) infrastructure.

```text
                  CUSTOMER SITES
                   /          \
              Site A          Site B
                 |               |
              CPE-A            CPE-B
                 |               |
              FNO-A            FNO-B
                 \               /
                  \             /
                    ISP EDGE
                       |
                    ISP CORE
                       |
                    CORE-SW
                  /    |     \
                 /     |      \
              IXP    DNS     TRANSIT
               |      |        |
           LOCAL WEB  DNS   GLOBAL WEB
                      SERVER
```

The architecture is a simplified educational representation of a multi-provider fibre service chain.

## Technologies

- **Cisco Packet Tracer** – Network topology simulation and connectivity testing.
- **Python 3.12** – Telemetry generation and analytical processing.
- **Pandas** – Data manipulation and analysis.
- **NumPy** – Numerical operations.
- **Matplotlib** – Data visualisation.
- **Git and GitHub** – Version control and project hosting.

## Main Features

1. Multi-domain network simulation.
2. Customer network segmentation.
3. Static routing and VLAN configuration.
4. DNS and HTTP service testing.
5. Customer network isolation using Access Control Lists (ACLs).
6. Controlled network fault scenarios.
7. Synthetic telemetry generation.
8. Rule-based fault classification.
9. Network performance analysis and visualisation.
10. Automated testing of Python components.

## Repository Structure

```text
FibreTrace/
│
├── data/              # Project datasets and generated telemetry
├── docs/              # Technical and project documentation
├── reports/           # Experimental results and analysis outputs
├── src/               # Python source code
├── tests/             # Automated tests
├── topology/          # Cisco Packet Tracer network topology
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/itspressly/FibreTrace.git
```

### 2. Enter the project directory

```bash
cd FibreTrace
```

### 3. Create a Python virtual environment

```bash
py -3.12 -m venv .venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install the dependencies

```bash
pip install -r requirements.txt
```

## Usage

The Python components can be run from the project root directory.

### Generate synthetic telemetry

```bash
python src/generate_telemetry.py
```

### Analyse telemetry

```bash
python src/analyze.py
```

### Run automated tests

```bash
python -m pytest tests/ -v
```

*Note: These commands assume the corresponding scripts and test files are present in the repository.*

## Cisco Packet Tracer

The network topology is provided in:

```text
topology/FibreTrace_V1.pkt
```

Open the file using Cisco Packet Tracer to inspect the simulated network.

The `docs/` directory contains supporting technical documentation and network configuration information.

## Experimental Results

The `reports/` directory is intended to contain experimental findings, network performance measurements, diagnostic outputs, and analytical results.

Results should be interpreted within the limitations of the simulated network and synthetic telemetry.

## Data Disclaimer

All generated telemetry used by FibreTrace is synthetic.

The Cisco Packet Tracer topology is a simplified educational simulation. It does not represent the confidential infrastructure, internal configurations, or live operational data of any telecommunications operator.

## Limitations

- The project does not directly collect live production telecommunications telemetry.
- Network experiments are conducted within a simulated environment.
- Fault classification is based on analytical rules rather than a production-grade network intelligence system.
- The project does not automatically control real telecommunications network devices.

## Future Improvements

- SNMP monitoring integration.
- Syslog collection.
- PostgreSQL telemetry storage.
- Additional dynamic routing protocols.
- Machine-learning-based anomaly detection.
- Interactive network monitoring dashboard.
- Integration with a real network testbed.

## Project Demonstration

A video demonstration can be added here to show the network topology, device configurations, connectivity tests, fault scenarios, and Python-based analysis.

**Video:** Add demonstration link when available.

## Author

**Pressly Zungunde**

BSc Information Technology  
Specialisation: Data Science

South Africa
