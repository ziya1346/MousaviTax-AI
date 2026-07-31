"""Tax advice API routes."""

from fastapi import APIRouter
from pydantic import BaseModel, Field

from agents.tax_advisor import TaxAdvisorAgent

router = APIRouter(prefix="/api/v1/tax", tags=["tax"])


class AdviseRequest(BaseModel):
    question: str = Field(..., min_length=3, max_length=2000, description="سؤال مالیاتی")


class AdviseResponse(BaseModel):
    answer: str
    agent: str
    version: str
    llm_live: bool


@router.post("/advise", response_model=AdviseResponse)
def advise(body: AdviseRequest) -> AdviseResponse:
    """دریافت مشاوره مالیاتی از Tax Advisor Agent."""
    agent = TaxAdvisorAgent()
    answer = agent.respond(body.question)
    info = agent.to_dict()
    return AdviseResponse(
        answer=answer,
        agent=info["name"],
        version=info["version"],
        llm_live=info["llm_live"],
    )
