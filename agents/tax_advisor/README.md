# Tax Advisor Agent

**ماژول:** MousaviTax AI (MEAP – Tax Module)  
**نسخه:** 0.1.0  
**وضعیت:** Skeleton (Sprint 01)

---

## نقش

این Agent مسئول **مشاوره مالیاتی اولیه** برای قوانین ایران است.

در Sprintهای بعدی به موارد زیر متصل می‌شود:
- AI Gateway / LLM Client
- RAG روی قوانین و بخشنامه‌ها (`knowledge/`)
- Tool Registry (محاسبات مالیاتی)
- Memory و Prompt Registry

---

## استفاده سریع

```python
from agents.tax_advisor import TaxAdvisorAgent

agent = TaxAdvisorAgent()
print(agent.respond("نرخ مالیات بر درآمد اشخاص حقیقی چقدر است؟"))
```

---

## ساختار

```text
agents/tax_advisor/
  __init__.py
  agent.py
  README.md
```

---

## Roadmap Agent

- [x] اسکلت پایه و System Prompt
- [ ] اتصال به LLM واقعی (Groq / OpenAI / ...)
- [ ] اتصال به RAG
- [ ] تعریف Tools
- [ ] ثبت در Agent Registry پلتفرم MEAP
