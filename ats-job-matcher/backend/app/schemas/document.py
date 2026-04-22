from pydantic import BaseModel


class DocumentGenerationRequest(BaseModel):
    job_title: str
    company: str
    job_description: str
    base_resume_text: str
    base_cover_letter_text: str | None = None


class DocumentGenerationResponse(BaseModel):
    tailored_resume_text: str
    tailored_cover_letter_text: str
    formats_available: list[str] = ["pdf", "docx"]
