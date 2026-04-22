from __future__ import annotations

from typing import Any

import httpx

from app.core.config import settings

BLOCKED_JOB_BOARD_PATTERNS = [
    "linkedin.com/jobs",
    "indeed.com",
    "ziprecruiter.com",
    "glassdoor.com",
    "monster.com",
]


def _build_queries(titles: list[str], locations: list[str], remote: bool) -> list[str]:
    queries: list[str] = []
    loc_clause = " OR ".join(locations) if locations else "United States"
    remote_clause = " remote" if remote else ""
    for title in titles:
        queries.append(f"site:.com careers {title} {loc_clause}{remote_clause}")
        queries.append(f"site:.com jobs {title} apply company {loc_clause}{remote_clause}")
    return queries


async def search_company_career_pages(titles: list[str], locations: list[str], remote: bool) -> list[dict[str, Any]]:
    queries = _build_queries(titles, locations, remote)
    all_results: list[dict[str, Any]] = []

    if settings.search_provider == "serpapi":
        for query in queries:
            params = {
                "engine": "google",
                "q": query,
                "api_key": settings.serpapi_api_key,
                "num": 10,
            }
            async with httpx.AsyncClient(timeout=30) as client:
                resp = await client.get("https://serpapi.com/search.json", params=params)
                resp.raise_for_status()
                payload = resp.json()
            for item in payload.get("organic_results", []):
                url = item.get("link", "")
                if _is_valid_company_job_url(url):
                    all_results.append(item)
        return all_results

    # Default: Bing Web Search API
    headers = {"Ocp-Apim-Subscription-Key": settings.bing_api_key}
    async with httpx.AsyncClient(timeout=30, headers=headers) as client:
        for query in queries:
            params = {"q": query, "count": 10, "responseFilter": "Webpages"}
            resp = await client.get(settings.bing_api_endpoint, params=params)
            resp.raise_for_status()
            payload = resp.json()
            for item in payload.get("webPages", {}).get("value", []):
                url = item.get("url", "")
                if _is_valid_company_job_url(url):
                    all_results.append(item)

    return all_results


def _is_valid_company_job_url(url: str) -> bool:
    lowered = url.lower()
    if not ("careers" in lowered or "/jobs" in lowered or "job" in lowered):
        return False
    if any(pattern in lowered for pattern in BLOCKED_JOB_BOARD_PATTERNS):
        return False
    return True
