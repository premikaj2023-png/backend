from pydantic import BaseModel
from typing import List

class AssessmentItem(BaseModel):
    id: int
    prompt: str

class AssessmentCreate(BaseModel):
    title: str
    language: str
    items: List[AssessmentItem]

class AssessmentResponse(BaseModel):
    assessmentId: str
    title: str
    language: str
    items: List[AssessmentItem]
