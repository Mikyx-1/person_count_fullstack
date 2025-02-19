from pydantic import BaseModel, Field
from datetime import datetime

class ImageUploadResponse(BaseModel):
    """Schema for API response after image processing"""
    imageUrl: str = Field(..., example="http://localhost:8000/uploads/image.jpg")
    peopleCount: int = Field(..., example=5)
    timestamp: datetime = Field(default_factory=datetime.utcnow)
