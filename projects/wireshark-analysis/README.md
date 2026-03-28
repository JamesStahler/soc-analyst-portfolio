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

![HTTP Traffic](./http-traffic.png)

![DNS Query](./dns-query.png)

![TCP Stream](./tcp-stream.png)

## Security Insight
- HTTP traffic is not encrypted and can be intercepted
- DNS queries reveal browsing behavior
- Packet analysis is critical for threat detection

## Outcome
Developed hands-on experience in packet analysis and network investigation.
