"""
Tax Advisor Agent – MousaviTax AI (MEAP Tax Module)

این Agent مسئول مشاوره مالیاتی اولیه است.
از packages.llm.LLMClient برای فراخوانی مدل استفاده می‌کند.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from packages.llm import LLMClient


@dataclass
class AgentMessage:
    role: str  # system | user | assistant
    content: str


@dataclass
class TaxAdvisorAgent:
    """Agent مشاوره مالیاتی."""

    name: str = "TaxAdvisor"
    role: str = "مشاور مالیاتی هوشمند ایران"
    version: str = "0.1.0"
    system_prompt: str = field(
        default=(
            "تو یک مشاور مالیاتی حرفه‌ای برای قوانین مالیاتی ایران هستی. "
            "پاسخ‌ها باید دقیق، مستند به قوانین و قابل‌اجرا باشند. "
            "اگر اطلاعات کافی نداری، صراحتاً بگو و سؤال تکمیلی بپرس."
        )
    )
    history: list[AgentMessage] = field(default_factory=list)
    llm: LLMClient | None = field(default=None)

    def __post_init__(self) -> None:
        if self.llm is None:
            self.llm = LLMClient()

    def reset(self) -> None:
        """پاک کردن تاریخچه گفتگو."""
        self.history.clear()

    def build_messages(self, user_input: str) -> list[dict[str, str]]:
        """ساخت لیست پیام برای ارسال به LLM."""
        messages = [{"role": "system", "content": self.system_prompt}]
        for msg in self.history:
            messages.append({"role": msg.role, "content": msg.content})
        messages.append({"role": "user", "content": user_input})
        return messages

    def respond(self, user_input: str) -> str:
        """دریافت پاسخ از LLM (یا حالت شبیه‌سازی)."""
        messages = self.build_messages(user_input)
        assert self.llm is not None
        reply = self.llm.chat(messages)

        self.history.append(AgentMessage(role="user", content=user_input))
        self.history.append(AgentMessage(role="assistant", content=reply))
        return reply

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "role": self.role,
            "version": self.version,
            "history_length": len(self.history),
            "llm_live": self.llm.is_live if self.llm else False,
            "llm_provider": self.llm.provider if self.llm else None,
        }


if __name__ == "__main__":
    agent = TaxAdvisorAgent()
    print(agent.respond("نرخ مالیات بر درآمد اشخاص حقیقی در سال ۱۴۰۴ چقدر است؟"))
    print(agent.to_dict())
