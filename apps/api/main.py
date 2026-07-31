from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.api.routes.tax import router as tax_router

app = FastAPI(
    title="MousaviTax AI",
    description="Tax Module of Mosavi Enterprise AI Platform (MEAP)",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tax_router)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "MousaviTax AI",
        "version": "0.1.0",
        "module": "tax",
        "platform": "MEAP",
    }


@app.get("/")
def root():
    return {
        "message": "MousaviTax AI – Tax Module of MEAP",
        "docs": "/docs",
        "endpoints": {
            "health": "/health",
            "tax_advise": "POST /api/v1/tax/advise",
        },
    }
