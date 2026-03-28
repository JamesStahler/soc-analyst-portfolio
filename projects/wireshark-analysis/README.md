# Wireshark Traffic Analysis Lab

## Objective
Analyzed network traffic using Wireshark to identify protocols, inspect packets, and understand how data moves across a network.

## Tools Used
- Wireshark
- Windows PC
- Web browser (to generate traffic)

## What I Did
- Captured live network traffic using Wireshark
- Applied filters:
  - http
  - dns
  - tcp
- Followed TCP streams to analyze full conversations

## Key Findings

### HTTP Traffic
Observed unencrypted web traffic and GET requests.

### DNS Queries
Captured domain name lookups and IP resolution.

### TCP Communication
Observed the TCP handshake (SYN, SYN-ACK, ACK).

## Screenshots

*Example of HTTP GET request showing unencrypted traffic*

*DNS query resolving a domain to an IP address*

*TCP stream showing full communication between client and server*

![HTTP Traffic](./http-traffic.png)

![DNS Query]([./dns-query.png](https://github.com/JamesStahler/soc-analyst-portfolio/blob/main/projects/wireshark-analysis/WIRESHARK-DNS.png))

![TCP Stream](./tcp-stream.png)

## Security Insight
- HTTP traffic is not encrypted and can be intercepted
- DNS queries reveal browsing behavior
- Packet analysis is critical for threat detection

## Outcome
Developed hands-on experience in packet analysis and network investigation.
# Wireshark Network Traffic Analysis & Packet Investigation

## Objective
...

## Tools Used
...

## What I Did
...

## Key Findings & Analysis
...

## SOC Relevance
...

## Screenshots
...

## Analyst Summary
This analysis demonstrates the ability to inspect network traffic, identify protocols, and evaluate potential security risks. While no malicious activity was detected, the workflow mirrors real-world SOC investigations where analysts must quickly determine whether traffic is normal or suspicious.
