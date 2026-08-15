# Nmap Network Scanning Lab

## Objective

Use Nmap through the Zenmap interface to identify listening TCP ports and services on an authorized local Windows test system, then evaluate the practical meaning of the results.

## Environment and Tools

- Nmap with Zenmap
- Windows computer
- Localhost target: 127.0.0.1

## Method

I ran Zenmap’s **Intense Scan** profile against localhost. This profile combines several Nmap capabilities, which may include host discovery, TCP port scanning, service and version detection, OS-detection attempts, and default NSE scripts depending on target permissions and responses.

Scanning localhost kept the activity within an authorized lab environment.

## Findings

The scan identified two listening TCP ports:

| Port | Common service | Interpretation |
|---|---|---|
| 135/tcp | Microsoft RPC | Supports communication among Windows services and management components |
| 445/tcp | Microsoft SMB | Supports Windows file sharing and related services |

Most other scanned ports were closed, indicating a limited number of listening services in the observed results.

## Analysis

Open ports are not vulnerabilities by themselves. Risk depends on the service configuration, software version, network exposure, authentication controls, patch status, and whether the service is necessary.

RPC and SMB are common in Windows environments but deserve careful control because externally exposed or unpatched services have historically been targeted by attackers.

## Security and Administration Considerations

- Disable unnecessary services.
- Restrict RPC and SMB access to trusted systems and networks.
- Block inappropriate external access with host and network firewalls.
- Keep Windows and related services patched.
- Monitor service exposure and investigate unexpected changes.
- Validate findings before assigning vulnerability severity.

## Skills Demonstrated

- Authorized host scanning
- TCP port and service identification
- Windows networking fundamentals
- Exposure analysis
- Secure configuration awareness
- Technical documentation

[← Back to all projects](../)
