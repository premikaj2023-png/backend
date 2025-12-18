from fastapi import APIRouter, UploadFile, File
from app.services.asr_service import speech_to_text
from app.services.report_service import generate_score

router = APIRouter()

@router.post("/audio")
async def upload_audio(file: UploadFile = File(...)):
    # Save file temporarily (mock)
    audio_path = f"/tmp/{file.filename}"

    transcript = speech_to_text(audio_path)
    result = generate_score(transcript)

    return {
        "filename": file.filename,
        "transcript": transcript,
        "score": result["score"],
        "feedback": result["feedback"]
    }
