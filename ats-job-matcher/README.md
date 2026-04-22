# ATS Job Matcher

Full-stack web application for uploading resumes, discovering jobs from company career pages, matching jobs against resume content, and generating ATS-optimized resumes/cover letters.

## Stack
- **Frontend:** Next.js 14 (App Router) + TypeScript
- **Backend:** FastAPI + Celery + Redis + PostgreSQL
- **AI:** OpenAI API (pluggable)
- **Search:** Bing Web Search API or SerpAPI (API-only; no direct search scraping)
- **Payments:** Stripe Checkout + Billing Portal

## Architecture

```
frontend (Next.js)
  -> calls backend REST API
backend (FastAPI)
  -> search providers (Bing/SerpAPI)
  -> parser + matcher + ats optimizer
  -> Redis cache + Celery queue
  -> PostgreSQL persistence
  -> Stripe billing/usage enforcement
```

## Quick Start

### 1) Backend
```bash
cd ats-job-matcher/backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8000
```

### 2) Frontend
```bash
cd ats-job-matcher/frontend
npm install
cp .env.local.example .env.local
npm run dev
```

## Core compliance choices
- Uses **API-based web search only**.
- Filters out known job boards and keeps company career domains.
- Contains crawler guardrails (`robots.txt` check + rate limiting placeholders).
- No CAPTCHA bypass logic.

## Pricing model implemented
- **Free:** 3 matches, basic optimization
- **Pay-as-you-go:** $2 per matched job package
- **Pro subscription:** $20/month, 100 matches/month and advanced optimization

## Future-ready modules included
- Auto-apply service skeleton (manual CAPTCHA only)
- Interview question generator hook
- LinkedIn optimizer hook
- Browser extension API hook
