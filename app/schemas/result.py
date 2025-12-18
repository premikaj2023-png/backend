from pydantic import BaseModel

class ResultResponse(BaseModel):
    sessionId: str
    transcript: str
    score: int
    feedback: str
