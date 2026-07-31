# MousaviTax AI

**ماژول مالیات هوشمند پلتفرم Mosavi Enterprise AI Platform (MEAP)**

Version: `0.1.0`  
Codename: `Foundation`  
Status: Sprint 01 – Infrastructure

---

## معرفی

MousaviTax AI هسته مشاوره و پردازش مالیاتی ایران است که به‌عنوان یکی از ماژول‌های کسب‌وکار (Business Module) به پلتفرم مادر **MEAP** متصل می‌شود.

### قابلیت‌های هدف (Roadmap)
- مشاوره مالیاتی هوشمند (Tax Advisor Agent)
- تحلیل اظهارنامه و قوانین مالیاتی ایران
- RAG روی قوانین، بخشنامه‌ها و رویه‌های مالیاتی
- اتصال به Accounting Core
- پشتیبانی از Multi-Agent (تحلیل‌گر، مشاور، بازرس)

---

## ساختار پروژه (Monorepo-ready)

```text
apps/
  api/                 # FastAPI service
services/
agents/
packages/
knowledge/             # قوانین و اسناد مالیاتی
tests/
docker/
docs/
scripts/
.github/
ai-governance/
```

---

## شروع سریع

```bash
git clone https://github.com/ziya1346/MousaviTax-AI.git
cd MousaviTax-AI

pip install -e .
uvicorn apps.api.main:app --reload

curl http://localhost:8000/health
```

---

## معماری

جزئیات در فایل [ARCHITECTURE.md](./ARCHITECTURE.md).

این ماژول از الگوی **Domain-Driven Design (DDD)** پیروی می‌کند و از **AI Core** مشترک پلتفرم MEAP استفاده می‌کند.

---

## استاندارد توسعه

```text
Issue → Branch → Commit → Pull Request → Review → Merge → Release
```

---

## لایه‌های پلتفرم MEAP

```text
Layer 1 – Infrastructure
Layer 2 – AI Core
Layer 3 – Business Modules   ← MousaviTax AI
Layer 4 – Applications
```

---

**نگهدارنده:** ziya1346  
**پلتفرم مادر:** Mosavi Enterprise AI Platform (MEAP)
