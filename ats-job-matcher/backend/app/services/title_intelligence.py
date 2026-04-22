from collections import defaultdict

# Expand user-entered titles to semantically close variants.
TITLE_SYNONYMS = {
    "soc analyst": [
        "Security Operations Analyst",
        "Cybersecurity Analyst",
        "Threat Analyst",
        "Incident Response Analyst",
    ],
    "security analyst": [
        "Cybersecurity Analyst",
        "Information Security Analyst",
        "SOC Analyst",
    ],
    "it support": ["Help Desk Analyst", "Technical Support Specialist", "Desktop Support Technician"],
}


def expand_job_titles(job_titles: list[str]) -> list[str]:
    expanded: dict[str, None] = defaultdict(lambda: None)

    for title in job_titles:
        clean = title.strip()
        if not clean:
            continue
        expanded[clean] = None
        for synonym in TITLE_SYNONYMS.get(clean.lower(), []):
            expanded[synonym] = None

    return list(expanded.keys())
