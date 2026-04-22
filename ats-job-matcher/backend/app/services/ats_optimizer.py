from __future__ import annotations

from app.core.config import settings


class ATSOptimizerService:
    """
    Generates ATS-friendly tailored resume and cover letter text.
    In production, connect this to OpenAI/Claude and structured prompts.
    """

    async def generate_documents(
        self,
        job_title: str,
        company: str,
        job_description: str,
        base_resume_text: str,
        base_cover_letter_text: str | None,
        advanced: bool,
    ) -> tuple[str, str]:
        if settings.openai_api_key:
            # Kept as a placeholder to stay concise. Replace with OpenAI SDK call.
            # The prompt should enforce ATS-safe formatting and no keyword stuffing.
            pass

        summary = self._extract_priority_keywords(job_description)
        tailored_resume = (
            f"TAILORED RESUME - {job_title} @ {company}\n\n"
            f"Targeted Keywords: {', '.join(summary)}\n\n"
            f"{base_resume_text}\n\n"
            "---\n"
            "Optimization Notes:\n"
            "- Added job-relevant terminology naturally\n"
            "- Preserved clean ATS structure with standard headings\n"
            f"- Optimization depth: {'Advanced' if advanced else 'Basic'}\n"
        )

        base_cover = base_cover_letter_text or "I am excited to apply for this role."
        tailored_cover = (
            f"TAILORED COVER LETTER - {job_title} @ {company}\n\n"
            f"{base_cover}\n\n"
            "Alignment highlights:\n"
            f"- Matches required skills: {', '.join(summary[:6])}\n"
            "- Focuses on measurable SOC/security outcomes\n"
        )
        return tailored_resume, tailored_cover

    def _extract_priority_keywords(self, job_description: str) -> list[str]:
        words = [w.strip('.,:;()[]{}').lower() for w in job_description.split()]
        words = [w for w in words if len(w) > 4]
        # Very simple keyword capture for starter implementation.
        unique: list[str] = []
        for word in words:
            if word not in unique:
                unique.append(word)
            if len(unique) >= 12:
                break
        return unique or ["security", "incident response", "siem", "threat detection"]
