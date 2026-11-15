
# FibreTrace
### Multi-Provider Fibre Fault Attribution and Service Assurance Platform

FibreTrace is a networking and data analytics portfolio
project designed to investigate connectivity failures
across a simulated telecommunications service chain.

The project combines Cisco Packet Tracer network
simulation with Python-based telemetry analysis and
rule-based fault classification.

## Project Objectives

- Simulate multiple customer connectivity environments.
- Represent separate hypothetical fibre access domains.
- Model ISP edge and core connectivity.
- Demonstrate IXP peering and upstream transit paths.
- Introduce and investigate network failures.
- Analyse network performance indicators.
- Identify likely fault domains.
- Produce diagnostic reports and visualisations.

## Architecture

Customer Sites
    |
FNO Access Domains
    |
ISP Edge
    |
ISP Core
   / \
 IXP Transit
  |    |
Local Global
Web   Web

An additional ISP services VLAN provides DNS.

## Technologies

- Cisco Packet Tracer
- Python 3.12
- Pandas
- NumPy
- Matplotlib
- Git
- GitHub

## Main Features

1. Multi-domain network simulation.
2. Static routing and VLAN segmentation.
3. DNS and HTTP service testing.
4. Customer network isolation using ACLs.
5. Controlled fault injection.
6. Synthetic telemetry generation.
7. Rule-based fault classification.
8. Performance visualisation.
9. Automated Python tests.

## Installation

Clone the repository:

git clone https://github.com/YOUR-USERNAME/FibreTrace.git

Move into the project directory:

cd FibreTrace

Create a virtual environment:

py -3.12 -m venv .venv

Activate it:

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

## Usage

Generate telemetry:

python src/generate_telemetry.py

Analyse the telemetry:

python src/analyze.py

Run tests:

python -m unittest discover -s tests -v

## Packet Tracer

Open:

topology/FibreTrace_V1.pkt

Follow docs/05-test-plan.md to reproduce the
network experiments.

## Results

The reports directory contains diagnostic outputs,
performance charts and experimental summaries.

## Data Disclaimer

The generated telemetry is synthetic.

The Packet Tracer network is a simplified educational
simulation and does not represent the confidential
infrastructure of any telecommunications operator.

## Limitations

FibreTrace does not directly collect production
telecommunications telemetry or automatically control
real network devices.

## Future Improvements

- SNMP monitoring integration.
- Syslog collection.
- PostgreSQL telemetry storage.
- Additional routing protocols.
- Machine-learning-based anomaly detection.
- Interactive monitoring dashboard.
- Real network testbed integration.

## Author

Pressly Zungunde

BSc Information Technology
Specialisation: Data Science

South Africa
