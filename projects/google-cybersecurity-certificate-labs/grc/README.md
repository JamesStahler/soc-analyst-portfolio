# Governance, Risk & Compliance (GRC) Coursework

This section contains selected Google Cybersecurity Professional Certificate projects involving risk assessment, security controls, compliance concepts, asset management, and threat modeling.

The projects demonstrate foundational ability to identify control gaps, organize risk findings, apply security frameworks, and communicate practical recommendations. They are educational exercises based on course-provided scenarios and templates.

---

## Featured Project: Botium Toys Security Audit

### Overview

I reviewed the security posture of the fictional Botium Toys organization by examining its assets, existing safeguards, risk exposure, and compliance considerations.

The course scenario assigned an overall risk score of **8/10 (high risk)** and presented gaps that could contribute to unauthorized access, data loss, regulatory exposure, and business disruption.

### Scope Reviewed

- Employee endpoints and internal infrastructure
- Business, e-commerce, and inventory systems
- Customer and payment information
- Data storage and retention
- Legacy systems
- Physical security controls

### Key Findings

- Excessive access to internally stored information
- Missing least-privilege controls and separation of duties
- Unencrypted customer credit-card data
- No intrusion detection system
- No disaster-recovery plan or backups of critical data
- Weak password requirements
- No centralized password-management system
- Inconsistent maintenance procedures for legacy systems
- Potential exposure of PII, SPII, and payment-card information

The scenario also identified existing safeguards, including firewall protection, antivirus monitoring, physical access controls, CCTV, and fire detection and prevention systems.

### Frameworks and Compliance Concepts

- NIST Cybersecurity Framework
- PCI DSS
- GDPR
- SOC 1 and SOC 2 concepts
- Personally Identifiable Information (PII)
- Sensitive Personally Identifiable Information (SPII)

> **Framework note:** The course scenario used the original five-function NIST CSF. NIST CSF 2.0 uses six functions: Govern, Identify, Protect, Detect, Respond, and Recover.

### Priority Recommendations

1. Apply least privilege and separation of duties.
2. Restrict access to PII, SPII, and payment-card information.
3. Encrypt sensitive data in transit and at rest.
4. Strengthen password requirements and centralize password management.
5. Deploy intrusion-detection capabilities.
6. Establish tested backups and disaster-recovery procedures.
7. Formalize maintenance procedures for legacy systems.
8. Perform recurring risk assessments, access reviews, asset inventories, and compliance reviews.

### Skills Demonstrated

- Risk and controls assessment
- Security-audit documentation
- NIST CSF fundamentals
- PCI DSS and GDPR concepts
- Risk prioritization
- Data classification and asset management
- Security recommendations and technical writing

### Artifacts

- [Botium Toys Scope, Goals & Risk Assessment](./botium-toys-scope-goals-risk-assessment%20(1).docx)
- [Controls & Compliance Checklist](./controls-and-compliance-checklist.docx)

---

## Additional Projects

### NIST SP 800-53 Data-Leak Analysis

Analyzed an information-disclosure scenario involving excessive permissions using **NIST SP 800-53 AC-6 (Least Privilege)**. The exercise covered access control, authorization, data-loss risk, and remediation recommendations.

[View the data-leak worksheet](./data-leak-worksheet.docx)

### PASTA Threat Modeling

Applied the PASTA methodology to a fictional application handling financial transactions. Identified business objectives, attack surfaces, injection and session-hijacking threats, vulnerabilities, risk-reduction controls, and PCI DSS considerations.

[View the PASTA worksheet](./pasta-threat-modeling-worksheet.docx)

### Security-Hardening Risk Assessment

Evaluated security weaknesses and recommended multi-factor authentication, stronger password policies, and recurring firewall maintenance to reduce unauthorized-access and brute-force risk.

[View the risk-assessment report](./security-risk-assessment-report.docx)

### Asset Inventory and Classification

Created an asset inventory and classified systems and information as restricted, confidential, internal-only, or public based on sensitivity and access needs.

[View the asset inventory](./home-asset-inventory.xlsx)

---

## Coursework Disclosure

The scenarios, organizational information, and some templates were provided through the Google Cybersecurity Professional Certificate. The completed assessments, classifications, analysis, and recommendations represent my coursework.

[← Back to Google certificate labs](../)
