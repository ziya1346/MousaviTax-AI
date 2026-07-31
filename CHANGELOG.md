# Changelog

All notable changes to MousaviTax AI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [0.1.0] - 2026-07-31

### Added
- Project structure aligned with MEAP (agents, knowledge, services, packages, docs, scripts, ai-governance, docker)
- FastAPI application with `/health` and root endpoints
- Docker Compose with PostgreSQL and Redis
- ARCHITECTURE.md, README.md, ROADMAP.md, SECURITY.md
- Tax Advisor Agent skeleton (`agents/tax_advisor`)
- LLM Client package (`packages/llm`) with Groq / OpenAI support and simulation mode
- Connection of TaxAdvisorAgent to LLMClient
- Basic unit tests for Tax Advisor Agent
- `.env.example` and expanded `pyproject.toml` / `.gitignore`
- Issue labels (feature, bug, documentation, security, ai, backend, frontend, database, high-priority)

### Changed
- Cleaned up previous skeleton and merge conflicts

### Notes
- Codename: Foundation
- Sprint 01 – Infrastructure
- Project Board pending additional GitHub connector permissions
