from __future__ import annotations

from io import BytesIO

from docx import Document
from pypdf import PdfReader


def extract_text_from_upload(filename: str, content: bytes) -> str:
    lowered = filename.lower()

    if lowered.endswith(".pdf"):
        reader = PdfReader(BytesIO(content))
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    if lowered.endswith(".docx"):
        doc = Document(BytesIO(content))
        return "\n".join(p.text for p in doc.paragraphs)

    if lowered.endswith(".doc"):
        # Legacy .doc parsing is intentionally shallow in this starter implementation.
        return content.decode(errors="ignore")

    raise ValueError("Unsupported file type. Use PDF/DOC/DOCX.")
