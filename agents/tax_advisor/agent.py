"""
Tax Advisor Agent – Skeleton for MousaviTax AI (MEAP Tax Module)

این Agent مسئول مشاوره مالیاتی اولیه است.
در Sprintهای بعدی به AI Core، RAG و Tool Registry متصل خواهد شد.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


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

    def respond(self, user_input: str, llm_response: str | None = None) -> str:
        """
        پاسخ ساده (بدون اتصال واقعی به LLM در این اسکلت).

        در نسخه‌های بعدی این متد به AI Gateway / LLM Client متصل می‌شود.
        """
        self.history.append(AgentMessage(role="user", content=user_input))

        if llm_response is None:
            # حالت شبیه‌سازی برای Sprint 01
            llm_response = (
                f"[TaxAdvisor v{self.version}] دریافت شد: «{user_input[:80]}...»\n"
                "این نسخه اسکلت است. در Sprint بعدی به مدل واقعی و RAG متصل خواهد شد."
            )

        self.history.append(AgentMessage(role="assistant", content=llm_response))
        return llm_response

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "role": self.role,
            "version": self.version,
            "history_length": len(self.history),
        }


if __name__ == "__main__":
    agent = TaxAdvisorAgent()
    print(agent.respond("نرخ مالیات بر درآمد اشخاص حقیقی در سال ۱۴۰۴ چقدر است؟"))
    print(agent.to_dict())
