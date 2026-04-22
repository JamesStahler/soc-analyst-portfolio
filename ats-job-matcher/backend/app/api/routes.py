from __future__ import annotations

from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from app.api.billing import router as billing_router
from app.schemas.document import DocumentGenerationRequest, DocumentGenerationResponse
from app.schemas.job import SearchResponse
from app.services.ats_optimizer import ATSOptimizerService
from app.services.file_parser import extract_text_from_upload
from app.services.job_service import rank_and_filter_jobs
from app.services.search_provider import search_company_career_pages
from app.services.title_intelligence import expand_job_titles

router = APIRouter()
optimizer = ATSOptimizerService()
router.include_router(billing_router)


@router.post("/jobs/search", response_model=SearchResponse, tags=["jobs"])
async def search_jobs(
    resume: UploadFile = File(...),
    cover_letter: UploadFile | None = File(default=None),
    job_titles: str = Form(...),
    locations: str = Form(default=""),
    remote: bool = Form(default=False),
    min_match_score: int = Form(default=60),
) -> SearchResponse:
    titles = [t.strip() for t in job_titles.split(",") if t.strip()]
    locs = [l.strip() for l in locations.split(",") if l.strip()]

    if not titles:
        raise HTTPException(
            status_code=400,
            detail="Please enter at least one job title (or use auto-suggest from resume).",
        )

    resume_text = extract_text_from_upload(resume.filename or "resume.pdf", await resume.read())

    expanded_titles = expand_job_titles(titles)
    raw_pages = await search_company_career_pages(expanded_titles, locs, remote)

    matched_jobs = rank_and_filter_jobs(
        resume_text=resume_text,
        job_pages=raw_pages,
        min_match_score=min_match_score,
        preferred_locations=locs,
    )

    return SearchResponse(expanded_titles=expanded_titles, matches=matched_jobs, total_matches=len(matched_jobs))


@router.post("/documents/generate", response_model=DocumentGenerationResponse, tags=["documents"])
async def generate_documents(payload: DocumentGenerationRequest) -> DocumentGenerationResponse:
    resume_text, cover_text = await optimizer.generate_documents(
        job_title=payload.job_title,
        company=payload.company,
        job_description=payload.job_description,
        base_resume_text=payload.base_resume_text,
        base_cover_letter_text=payload.base_cover_letter_text,
        advanced=True,
    )

    return DocumentGenerationResponse(
        tailored_resume_text=resume_text,
        tailored_cover_letter_text=cover_text,
        formats_available=["pdf", "docx"],
    )
