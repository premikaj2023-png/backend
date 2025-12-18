from fastapi import APIRouter
from app.schemas.session import SessionCreate, SessionResponse
from app.schemas.result import ResultResponse
import uuid

router = APIRouter()

SESSIONS = {}

@router.post("/", response_model=SessionResponse)
def start_session(data: SessionCreate):
    session_id = str(uuid.uuid4())

    SESSIONS[session_id] = {
        "sessionId": session_id,
        "assessmentId": data.assessmentId,
        "studentId": data.studentId,
        "status": "in_progress"
    }

    return {
        "sessionId": session_id,
        "status": "in_progress"
    }

@router.get("/{session_id}/results", response_model=ResultResponse)
def get_results(session_id: str):
    # mock AI output
    return {
        "sessionId": session_id,
        "transcript": "Mock transcript of speech",
        "score": 88,
        "feedback": "Good pronunciation, minor stress issues"
    }
