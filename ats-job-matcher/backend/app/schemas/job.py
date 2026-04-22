from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
    job_titles: list[str] = Field(default_factory=list)
    locations: list[str] = Field(default_factory=list)
    remote: bool = False
    min_match_score: int = 60


class JobResult(BaseModel):
    title: str
    company: str
    location: str | None = None
    apply_url: str
    description: str
    match_score: float
    freshness: str | None = None


class SearchResponse(BaseModel):
    expanded_titles: list[str]
    matches: list[JobResult]
    total_matches: int
