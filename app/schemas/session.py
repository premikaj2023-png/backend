from pydantic import BaseModel

class SessionCreate(BaseModel):
    assessmentId: str
    studentId: str

class SessionResponse(BaseModel):
    sessionId: str
    status: str
