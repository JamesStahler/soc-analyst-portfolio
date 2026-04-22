from __future__ import annotations

import re
from collections import Counter

from rapidfuzz import fuzz


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-zA-Z][a-zA-Z0-9+#.-]{1,}", text.lower())


def top_keywords(text: str, max_keywords: int = 80) -> list[str]:
    tokens = tokenize(text)
    filtered = [t for t in tokens if len(t) > 2]
    counts = Counter(filtered)
    return [term for term, _ in counts.most_common(max_keywords)]


def score_job_match(resume_text: str, job_description: str, title_bonus: float = 0.0) -> float:
    resume_keywords = set(top_keywords(resume_text))
    job_keywords = set(top_keywords(job_description))

    if not job_keywords:
        return 0.0

    overlap = len(resume_keywords.intersection(job_keywords))
    keyword_score = (overlap / max(len(job_keywords), 1)) * 100

    semantic_score = fuzz.token_set_ratio(resume_text[:5000], job_description[:5000])

    # Blend lexical and fuzzy similarity, then apply optional title relevance bonus.
    final_score = (0.65 * keyword_score) + (0.35 * semantic_score) + title_bonus
    return round(min(final_score, 100.0), 2)
