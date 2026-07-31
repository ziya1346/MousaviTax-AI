"""
LLM Client – MousaviTax AI

Supports Groq and OpenAI. Falls back to simulation mode when no API key is set.
"""

from __future__ import annotations

import os
from typing import Any


class LLMClient:
    def __init__(
        self,
        provider: str | None = None,
        model: str | None = None,
    ) -> None:
        self.provider = (provider or os.getenv("LLM_PROVIDER", "groq")).lower()
        self.model = model or os.getenv(
            "LLM_MODEL",
            "llama-3.3-70b-versatile" if self.provider == "groq" else "gpt-4o-mini",
        )
        self._client: Any = None
        self._init_client()

    def _init_client(self) -> None:
        if self.provider == "groq":
            api_key = os.getenv("GROQ_API_KEY")
            if api_key:
                try:
                    from groq import Groq

                    self._client = Groq(api_key=api_key)
                except ImportError:
                    self._client = None
        elif self.provider == "openai":
            api_key = os.getenv("OPENAI_API_KEY")
            if api_key:
                try:
                    from openai import OpenAI

                    self._client = OpenAI(api_key=api_key)
                except ImportError:
                    self._client = None

    @property
    def is_live(self) -> bool:
        return self._client is not None

    def chat(
        self,
        messages: list[dict[str, str]],
        temperature: float = 0.4,
        max_tokens: int = 2048,
    ) -> str:
        if not self._client:
            last_user = next(
                (m["content"] for m in reversed(messages) if m["role"] == "user"),
                "",
            )
            return (
                f"[SIMULATION – {self.provider}/{self.model}]\n"
                f"دریافت شد: {last_user[:120]}...\n"
                "کلید API تنظیم نشده. برای پاسخ واقعی GROQ_API_KEY یا OPENAI_API_KEY را در .env قرار دهید."
            )

        try:
            response = self._client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return response.choices[0].message.content or ""
        except Exception as exc:
            return f"خطا در فراخوانی LLM: {exc}"
