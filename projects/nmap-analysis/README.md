# Nmap Network Scanning Lab (Zenmap GUI)

## Objective
The objective of this lab was to perform network reconnaissance using Nmap (via the Zenmap GUI) to identify open ports, detect running services, and better understand how systems expose network services during a scan.

---

## Tools Used
- Nmap (Zenmap GUI)
- Windows Operating System
- Localhost (127.0.0.1) test environment

---

## Methodology
I utilized the Zenmap graphical interface to perform an **Intense Scan** against the local machine (127.0.0.1). 

The Intense Scan profile includes:
- TCP SYN scan (stealth scan)
- Service/version detection
- OS detection
- Default script scanning

This allowed for a more comprehensive view of the system’s network exposure compared to a basic scan.

---

## Scan Configuration
- **Target:** 127.0.0.1 (localhost)
- **Profile Used:** Intense Scan
- **Underlying Command:**

- 
---

## Findings
The scan identified the following open ports:

- **135/tcp (RPC)** – Microsoft Remote Procedure Call service
- **445/tcp (SMB)** – Microsoft Directory Services (file sharing)

Most other scanned ports were closed, indicating limited exposed services on the system.

---

## Analysis
Port 135 (RPC) is commonly used for communication between Windows services and can be leveraged for remote management.

Port 445 (SMB) is used for file and printer sharing. This port is frequently targeted in cyberattacks (e.g., ransomware exploits like WannaCry) if improperly secured.

The presence of these ports is typical for Windows systems, but they should be monitored and restricted when exposed to external networks.

---

## Security Considerations
- Unnecessary services should be disabled when not in use
- SMB access should be restricted to trusted networks
- Firewalls should be configured to block external access to sensitive ports
- Systems should be regularly updated to prevent known vulnerabilities

---

## Conclusion
This lab demonstrated how to use Nmap (via Zenmap) to perform effective network reconnaissance, identify exposed services, and evaluate potential security risks associated with open ports.

## Skills Demonstrated
- Network Scanning (Nmap / Zenmap)
- Port & Service Identification
- OS & Service Enumeration
- Basic Vulnerability Awareness
- Network Security Analysis
