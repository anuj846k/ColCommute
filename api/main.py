"""FastAPI app entrypoint."""

from fastapi import FastAPI

from api.routers.auth import router as auth_router

app = FastAPI(title="ColCommute API", version="0.1.0")
app.include_router(auth_router)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
