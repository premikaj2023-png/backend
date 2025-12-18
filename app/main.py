from fastapi import FastAPI
from app.api import assessments, sessions, upload

app = FastAPI(title="Speech Assessment Platform")

app.include_router(assessments.router, prefix="/assessments", tags=["Assessments"])
app.include_router(sessions.router, prefix="/sessions", tags=["Sessions"])
app.include_router(upload.router, prefix="/upload", tags=["Upload"])

@app.get("/")
def health():
    return {"status": "Backend running"}
