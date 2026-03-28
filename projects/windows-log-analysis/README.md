# Windows Security Log Analysis – Failed Login Investigation

## Objective
Analyzed Windows Security logs in Event Viewer to identify failed login attempts and understand how authentication events are recorded in Windows.

## Tools Used
- Windows Event Viewer
- Windows Security Logs
- Windows 11

## What I Did
- Opened Event Viewer and navigated to Windows Logs > Security
- Reviewed security events related to login activity
- Identified Event ID 4625 as a failed logon event
- Examined event information such as logon type, account details, and audit status

## Key Findings & Analysis
- Located failed login attempts recorded as Event ID 4625
- Observed Audit Failure entries associated with unsuccessful authentication attempts
- Reviewed event metadata including time, log source, and task category
- Confirmed Logon Type 2, which indicates an interactive logon attempt at the local system

## Threat Hunting Perspective
- Reviewed failed authentication activity to understand how suspicious login behavior may appear in Windows logs
- Looked for repeated failed logon attempts that could indicate unauthorized access attempts
- No confirmed malicious activity was identified in this review, but the workflow reflects a real log investigation process

## SOC Relevance
This type of analysis reflects real SOC responsibilities, including:
- Monitoring authentication logs
- Investigating failed login attempts
- Detecting possible unauthorized access activity
- Supporting incident response through Windows event log analysis

## Screenshots

![Security Log Overview](./security-log-overview.png)

![Event ID 4625 Selected](./event-4625-selected.png)

![Failed Login Event Details](./failed-login-details.png)

## Analyst Summary
This project demonstrates the ability to review Windows Security logs, identify failed authentication events, and interpret host-based log data in a way that supports security monitoring and investigation workflows.
