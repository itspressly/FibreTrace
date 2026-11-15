

# FibreTrace Security and Limitations

## 1. Introduction

Security is an important part of FibreTrace because the project represents a network environment where multiple customer sites share parts of an ISP infrastructure.

This document explains the security measures included in the prototype, the limitations of the simulation and the precautions that would be required before using a similar system in a real network.

## 2. Customer Network Separation

FibreTrace uses Access Control Lists (ACLs) on the ISP edge router to control traffic between the two customer networks.

The two customer networks are:

- Site A: `10.10.10.0/24`
- Site B: `10.20.20.0/24`

The ACL rules prevent direct communication between the two customer networks while allowing traffic towards other permitted destinations.

This demonstrates how an ISP can apply traffic separation policies to protect customers who use shared network infrastructure.

The ACL configuration is applied to the ISP edge router interfaces connected to the two FNO networks.

## 3. Private Network Addressing

The project uses private IP address ranges for internal customer and network infrastructure.

These include:

- `10.10.10.0/24`
- `10.20.20.0/24`
- `10.50.50.0/24`

Private addressing helps organise internal networks and prevents these addresses from being directly routed across the public internet.

## 4. Reserved Documentation IP Addresses

The prototype also uses reserved IP address ranges to represent public-facing services.

These include:

- `198.51.100.0/24` for the local web server network.
- `203.0.113.0/24` for the global web server network.

These ranges are reserved for documentation and examples. They are not intended to represent real public internet addresses.

## 5. Lab Credentials

Any usernames and passwords used in the Packet Tracer environment are for laboratory testing only.

They must not be reused as production credentials.

A real deployment would require strong passwords, controlled access, secure authentication and regular credential management.

Credentials should not be included in public documentation or uploaded to a public repository.

## 6. Lack of Production Telemetry

FibreTrace currently does not collect live telemetry from an ISP or Fibre Network Operator.

The project uses a simulated network environment and experimental observations.

It therefore cannot currently monitor real customer connections or provide live fault notifications for operational networks.

## 7. Lack of Real Fibre Optical Measurements

Packet Tracer does not provide actual fibre-optic measurements such as:

- Optical signal power.
- Optical signal loss.
- Fibre attenuation.
- Optical module temperature.
- Physical fibre faults.

These measurements would be important in a real fibre monitoring environment.

The current prototype focuses on network connectivity and service-level observations rather than physical fibre diagnostics.

## 8. Packet Tracer Limitations

Cisco Packet Tracer provides a useful environment for learning and testing network configurations. However, it is a simulation tool.

Its behaviour does not represent every detail of real network hardware, ISP infrastructure or fibre transmission systems.

Some advanced routing, monitoring and hardware-level features may not be available or may behave differently from real equipment.

## 9. Synthetic Data

Some observations used for Python analysis may be generated or simulated to represent different network conditions.

Synthetic data is useful for developing and testing the analytical component, but it does not automatically represent real-world network behaviour.

The project must clearly distinguish between simulated observations and measurements collected from actual equipment.

## 10. Protecting Real Operational Data

If FibreTrace is extended for use by an ISP or enterprise network team, additional security measures would be necessary.

These should include:

- Secure communication between monitoring systems and network devices.
- Authentication and role-based access control.
- Encryption of sensitive information.
- Secure storage of telemetry and customer information.
- Access logging and monitoring.
- Regular backups and security updates.
- Protection of customer identities and network configurations.

Real operational and customer data must only be collected and processed with proper authorisation.

## 11. Conclusion

FibreTrace demonstrates basic network separation, connectivity monitoring and experimental fault analysis in a controlled environment.

However, it remains a prototype. Its current capabilities should not be confused with a fully deployed ISP monitoring platform.

Further development, testing and security improvements would be required before real-world deployment.

