# Governance, Risk & Compliance (GRC) Portfolio

This section of my cybersecurity portfolio contains hands-on projects focused on governance, cybersecurity risk management, security controls, compliance, asset management, and threat modeling.

These projects were completed during the Google Cybersecurity Professional Certificate and demonstrate my ability to evaluate security risks, identify control gaps, apply cybersecurity frameworks and compliance concepts, and communicate security recommendations from a business-risk perspective.

---

# 🛡️ Featured Project: Botium Toys Security Audit

## Security Audit, Risk Assessment & Compliance Review

### Project Overview

In this project, I evaluated the security posture of a fictional organization, Botium Toys, by reviewing its assets, existing security controls, risk exposure, and compliance practices.

The assessment identified significant gaps in technical and administrative controls that increased the organization's exposure to data loss, unauthorized access, regulatory penalties, and business disruption.

**Overall Risk Score: 8/10 — High Risk**

### Audit Scope

The assessment covered:

- Employee endpoints and equipment
- Internal network infrastructure
- Business systems and software
- E-commerce and inventory systems
- Customer and payment information
- Data storage and retention
- Legacy systems
- Physical security controls

### Key Risk Findings

The assessment identified several significant security gaps:

- Excessive employee access to internally stored information
- Lack of least-privilege access controls
- Lack of separation of duties
- Customer credit-card data was not encrypted
- No intrusion detection system (IDS)
- No disaster recovery plan
- No backups of critical business data
- Weak password requirements
- No centralized password-management system
- Inconsistent maintenance procedures for legacy systems
- Potential exposure of PII/SPII and payment-card information

Existing safeguards included firewall protection, antivirus monitoring, physical access controls, CCTV surveillance, and fire detection/prevention systems.

### Governance & Compliance Areas Reviewed

The assessment considered security and privacy requirements and concepts associated with:

- NIST Cybersecurity Framework (NIST CSF)
- PCI DSS
- GDPR
- SOC 1 / SOC 2 concepts
- Personally Identifiable Information (PII)
- Sensitive Personally Identifiable Information (SPII)

> **Framework note:** The Google course scenario referenced the five-function version of the NIST Cybersecurity Framework. The current NIST CSF 2.0 uses six functions: Govern, Identify, Protect, Detect, Respond, and Recover.

### Recommended Security Improvements

Based on the assessment, priority improvements include:

1. Implement least-privilege access controls.
2. Establish separation of duties for sensitive systems and information.
3. Restrict access to customer PII/SPII and payment-card information to authorized personnel.
4. Encrypt sensitive customer and payment-card data both in transit and at rest.
5. Strengthen password requirements and implement centralized password management.
6. Deploy an intrusion detection system (IDS).
7. Establish regular backups of critical data.
8. Develop and test a disaster recovery plan.
9. Document maintenance schedules and intervention procedures for legacy systems.
10. Conduct regular risk assessments, access reviews, asset inventories, and compliance reviews.

### Skills Demonstrated

- Governance, Risk & Compliance (GRC)
- Cybersecurity Risk Assessment
- Security Auditing
- Controls Assessment
- Compliance Analysis
- NIST Cybersecurity Framework
- PCI DSS
- GDPR
- Risk Identification & Prioritization
- Security Control Recommendations
- Data Classification
- Asset Management
- Security Documentation

### Project Artifacts

- [Botium Toys Scope, Goals & Risk Assessment](./botium-toys-scope-goals-risk-assessment%20(1).docx)
- [Controls & Compliance Checklist](./controls-and-compliance-checklist.docx)

---

# Additional GRC & Risk Projects

## NIST SP 800-53 Data Leak Analysis

Analyzed an information disclosure scenario involving excessive access permissions and evaluated the incident using **NIST SP 800-53 AC-6 (Least Privilege)**.

Focus areas included:

- Access control
- Least privilege
- Data-loss prevention
- User authorization
- Remediation recommendations

Artifact: [Data Leak Worksheet](./data-leak-worksheet.docx)

## PASTA Threat Modeling

Applied the **PASTA threat-modeling methodology** to an application environment involving financial transactions.

Identified:

- Business and security objectives
- Technical attack surface
- Injection and session-hijacking threats
- Application vulnerabilities
- Risk-reduction controls
- PCI DSS considerations

Artifact: [PASTA Threat Modeling Worksheet](./pasta-threat-modeling-worksheet.docx)

## Security Hardening Risk Assessment

Evaluated security weaknesses and recommended controls such as:

- Multi-factor authentication (MFA)
- Strong password policies
- Regular firewall maintenance

Recommendations were evaluated according to their ability to reduce unauthorized access and brute-force attack risk.

Artifact: [Security Risk Assessment Report](./security-risk-assessment-report.docx)

## Asset Inventory & Classification

Created an asset inventory and classified information systems according to sensitivity and access requirements.

Classification categories included:

- Restricted
- Confidential
- Internal-only
- Public

Artifact: [Home Asset Inventory](./home-asset-inventory.xlsx)

---

## About These Projects

These projects were completed as part of the Google Cybersecurity Professional Certificate.

Some scenarios, organizational information, and document templates were provided as part of the course. The completed assessments, classifications, analysis, and recommendations represent coursework performed to demonstrate practical cybersecurity and GRC concepts.
