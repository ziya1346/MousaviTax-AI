# Architecture – MousaviTax AI

**Version:** 0.1.0  
**Module:** Tax (Business Module)  
**Parent Platform:** Mosavi Enterprise AI Platform (MEAP)

---

## 1. جایگاه در پلتفرم

MousaviTax AI در **Layer 3 – Business Modules** قرار دارد و از طریق AI Core (Layer 2) به زیرساخت مشترک متصل می‌شود.

```
┌─────────────────────────────────────────────┐
│              Applications (Layer 4)          │
├─────────────────────────────────────────────┤
│  Tax Module │ Accounting │ Travel │ Legal   │  ← Layer 3
├─────────────────────────────────────────────┤
│         AI Core (Gateway, RAG, Agents)      │  ← Layer 2
├─────────────────────────────────────────────┤
│     Infrastructure (DB, Redis, MinIO...)    │  ← Layer 1
└─────────────────────────────────────────────┘
```

---

## 2. اصول معماری

- **Domain-Driven Design (DDD)**  
  مرز مشخص دامنه مالیات، مدل داده مستقل و قوانین اختصاصی.
- **Loose Coupling**  
  ارتباط با سایر ماژول‌ها فقط از طریق API یا Event.
- **Shared AI Core**  
  استفاده مشترک از Prompt Engine، Memory، RAG، Model Registry و Agent Registry.
- **API-First**  
  تمام قابلیت‌ها از طریق FastAPI در دسترس هستند.

---

## 3. اجزای اصلی ماژول

| جزء | توضیح |
|-----|--------|
| `apps/api` | سرویس FastAPI |
| `agents/` | Tax Advisor، Analyzer، Auditor |
| `knowledge/` | قوانین، بخشنامه‌ها، رویه‌ها (منبع RAG) |
| `packages/` | مدل‌های دامنه و utilityهای مشترک |
| `services/` | منطق کسب‌وکار |

---

## 4. ارتباط با AI Core

- ثبت Agentها در **Agent Registry**
- استفاده از **Prompt Registry**
- اتصال به **RAG** برای بازیابی قوانین
- گزارش مصرف مدل در **AI-BOM**

---

## 5. استقرار (Deployment)

- Docker Compose برای توسعه محلی
- PostgreSQL برای داده‌های ساختاریافته
- Qdrant / pgvector برای Vector Store
- Redis برای Cache و Session

---

## 6. امنیت

- احراز هویت از طریق پلتفرم مادر
- جداسازی داده حساس مالیاتی
- رعایت اصول AI Governance

---

**وضعیت:** Foundation (Sprint 01)
