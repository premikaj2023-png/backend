from fastapi import APIRouter
from app.schemas.assessment import AssessmentCreate, AssessmentResponse
import uuid

router = APIRouter()

# mock DB
ASSESSMENTS = {}

@router.post("/", response_model=AssessmentResponse)
def create_assessment(data: AssessmentCreate):
    assessment_id = str(uuid.uuid4())

    assessment = {
        "assessmentId": assessment_id,
        "title": data.title,
        "language": data.language,
        "items": data.items
    }

    ASSESSMENTS[assessment_id] = assessment
    return assessment

@router.get("/{assessment_id}", response_model=AssessmentResponse)
def get_assessment(assessment_id: str):
    return ASSESSMENTS[assessment_id]
