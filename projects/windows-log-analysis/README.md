# Windows Security Log Analysis: Failed Logon Investigation

## Objective

Use Windows Event Viewer to locate and interpret failed authentication activity and document a repeatable first-pass investigation workflow.

## Environment and Tools

- Windows 11
- Windows Event Viewer
- Windows Security log

## Investigation Steps

1. Opened Event Viewer and navigated to **Windows Logs > Security**.
2. Filtered and reviewed events associated with authentication activity.
3. Identified **Event ID 4625**, which records a failed account logon.
4. Examined the timestamp, audit status, account fields, logon type, source details, and failure information.
5. Checked surrounding activity for repeated failures or other indicators requiring escalation.

## Findings

- Located an Audit Failure entry recorded as Event ID 4625.
- Confirmed **Logon Type 2**, indicating an interactive attempt at the local system.
- Reviewed the available account and event metadata to understand the context of the failure.
- Did not identify confirmed malicious activity in the captured evidence.

## Operational Relevance

Failed-logon analysis can support:

- Windows endpoint troubleshooting
- Account and access investigations
- Detection of repeated authentication failures
- Initial security triage
- Incident documentation and escalation

A single failed logon does not prove malicious activity. Additional context—such as frequency, source, affected accounts, timing, and related events—is needed before drawing that conclusion.

## Evidence

![Windows Security log overview](./security-log-overview.png)

![Event ID 4625 selected](./event-4625-selected.png)

![Failed logon event details](./failed-login-details.png)

## Skills Demonstrated

- Windows Event Viewer
- Authentication-event analysis
- Event ID interpretation
- Evidence-based investigation
- Technical documentation

[← Back to all projects](../)
