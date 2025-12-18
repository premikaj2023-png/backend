from fastapi import FastAPI
from app.api import assessments, sessions, upload

app = FastAPI(title="Speech Assessment API")

app.include_router(assessments.router, prefix="/assessments")
app.include_router(sessions.router, prefix="/sessions")
app.include_router(upload.router, prefix="/upload")

@app.get("/")
def health():
    return {"status": "Backend running"}
