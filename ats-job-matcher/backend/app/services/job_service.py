from __future__ import annotations

from urllib.parse import urlparse

from app.schemas.job import JobResult
from app.services.matching_engine import score_job_match


def company_from_url(url: str) -> str:
    host = urlparse(url).netloc.replace("www.", "")
    return host.split(".")[0].title() if host else "Unknown"


def rank_and_filter_jobs(
    resume_text: str,
    job_pages: list[dict],
    min_match_score: int,
    preferred_locations: list[str],
) -> list[JobResult]:
    results: list[JobResult] = []

    for item in job_pages:
        title = item.get("name") or item.get("title") or "Untitled Role"
        url = item.get("url") or item.get("link")
        snippet = item.get("snippet") or item.get("description") or ""
        if not url:
            continue

        score = score_job_match(resume_text, snippet)
        if score < min_match_score:
            continue

        location = _guess_location(snippet)
        loc_bonus = 2.5 if _location_relevant(location, preferred_locations) else 0

        results.append(
            JobResult(
                title=title,
                company=company_from_url(url),
                location=location,
                apply_url=url,
                description=snippet,
                match_score=round(min(score + loc_bonus, 100.0), 2),
                freshness=item.get("dateLastCrawled"),
            )
        )

    return sorted(results, key=lambda x: x.match_score, reverse=True)


def _guess_location(text: str) -> str | None:
    candidates = ["Remote", "New York", "Austin", "Chicago", "San Francisco", "United States"]
    lowered = text.lower()
    for c in candidates:
        if c.lower() in lowered:
            return c
    return None


def _location_relevant(location: str | None, preferred_locations: list[str]) -> bool:
    if not preferred_locations or not location:
        return False
    return any(p.lower() in location.lower() for p in preferred_locations)
