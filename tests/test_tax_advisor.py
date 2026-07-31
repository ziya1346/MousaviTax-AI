"""Tests for Tax Advisor Agent."""

from agents.tax_advisor import TaxAdvisorAgent


def test_agent_creation():
    agent = TaxAdvisorAgent()
    assert agent.name == "TaxAdvisor"
    assert agent.version == "0.1.0"


def test_agent_respond_simulation():
    agent = TaxAdvisorAgent()
    reply = agent.respond("سلام")
    assert isinstance(reply, str)
    assert len(reply) > 0
    assert len(agent.history) == 2


def test_agent_reset():
    agent = TaxAdvisorAgent()
    agent.respond("تست")
    agent.reset()
    assert len(agent.history) == 0


def test_agent_to_dict():
    agent = TaxAdvisorAgent()
    data = agent.to_dict()
    assert data["name"] == "TaxAdvisor"
    assert "llm_live" in data
