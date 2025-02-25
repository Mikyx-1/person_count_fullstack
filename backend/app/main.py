from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import shutil
from pathlib import Path
from .add_data import add_person_data
from .models import SessionLocal, PersonData
from .schemas import ImageUploadResponse
import cv2
from .count import count_person_in_img
from .endpoints import router as history_router

app = FastAPI()
db_session = SessionLocal()

# Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(history_router)
# Ensure directories exist
Path("uploads").mkdir(parents=True, exist_ok=True)
Path("results").mkdir(parents=True, exist_ok=True)

# Serve static files for uploaded images and results
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.mount("/results", StaticFiles(directory="results"), name="results")

@app.post("/upload", response_model=ImageUploadResponse)
async def upload_image(file: UploadFile = File(...)):
    """Handles image upload, performs detection, and saves results in a separate folder."""
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Only JPEG and PNG images are allowed.")
    
    # Save original image to uploads/
    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Read image & perform detection
    image = cv2.imread(file_location)
    if image is None:
        raise HTTPException(status_code=400, detail="Invalid image file.")

    people_count, visualized_img = count_person_in_img(image)

    # Save the visualized image in results/
    visualized_img_path = f"results/processed_{file.filename}"
    cv2.imwrite(visualized_img_path, visualized_img)

    # Save results to database
    add_person_data(db_session, people_count, visualized_img_path)

    # Return API response with validation
    return ImageUploadResponse(
        imageUrl=f"http://localhost:8000/results/processed_{file.filename}",
        peopleCount=people_count
    )
