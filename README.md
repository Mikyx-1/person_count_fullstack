# Person Counter Web App

## 📌 Overview
This is a **Person Counter Web Application** that allows users to upload an image, detect the number of people present, and visualise the detected bounding boxes. The results, including the processed image and count, are stored in a **PostgreSQL database**. The application consists of a **FastAPI** backend and a **Next.js** frontend, deployed using **Docker Compose**.

![Screenshot from 2025-02-19 08-24-42](https://github.com/user-attachments/assets/3183f68d-4435-49c3-b94a-3afa676d3c43)

## 🏗️ Architecture

The application follows a **client-server architecture**:

- **Frontend:** Built with Next.js to provide a user-friendly interface for uploading images and displaying detection results.
- **Backend:** Built with FastAPI, handling image processing and database operations.
- **Database:** PostgreSQL with SQLAlchemy for storing detection results.
- **Deployment:** Docker Compose for easy containerised deployment.

## 🖥️ Algorithm
The system uses **OpenCV and a person detection model** for image processing:

1. **Image Upload**: Users upload an image through the frontend.
2. **Preprocessing**: The image is sent to the FastAPI backend, where it is validated and saved.
3. **Person Detection**: OpenCV or a deep learning model (like YOLO, SSD, or Haar Cascades) detects people in the image.
4. **Bounding Box Visualisation**: Detected people are marked with bounding boxes on the image.
5. **Result Storage**:
   - The visualized image is saved in a `results/` folder.
   - The detection count and image path are stored in PostgreSQL.
6. **Response to Frontend**: The processed image and person count are sent back and displayed in the UI.

## 🚀 How to Run the Application

### 1️⃣ Prerequisites
Ensure you have the following installed:
- **Docker & Docker Compose**
- **Python 3.7+** (if running locally)
- **Node.js 20+** (for the frontend)

### 2️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/person-detection-app.git
cd person-detection-app
```

### 3️⃣ Setup Environment Variables
Create a `.env` file in the root directory and configure it with database details:
```sh
DATABASE_URL=postgresql://user:password@db:5432/person_detection_db
```

### 4️⃣ Run with Docker (Recommended)
```sh
docker-compose up --build
```
This will start the **backend, frontend, and database** services.

### 5️⃣ Run Locally (Alternative Method)
#### Backend (FastAPI)
```sh
cd backend
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate the virtual environment (Linux/macOS)
venv\Scripts\activate  # (Windows)
pip install -r requirements.txt  # Install dependencies
uvicorn backend.app.main:app --reload
```

#### Frontend (Next.js)
```sh
cd frontend
npm install  # Install dependencies
npm run dev  # Start the development server
```

### 6️⃣ Access the Application
- **Frontend UI**: [http://localhost:3000](http://localhost:3000)
- **Backend API Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)

## 📂 Folder Structure
```
PERSON-DETECTION/
├── backend/          # FastAPI backend
│   ├── app/
│   │   ├── models.py  # Database models
│   │   ├── count.py   # Person detection logic
│   │   ├── main.py    # API endpoints
│   │   ├── schemas.py # API data validation
│   └── ...
├── frontend/         # Next.js frontend
│   ├── components/ui # UI components
│   ├── app/page.tsx  # Main page
│   └── ...
├── docker-compose.yml # Docker configuration
├── .env              # Environment variables
└── README.md         # Project documentation
```

## 🎯 API Endpoints
| Method | Endpoint  | Description |
|--------|----------|-------------|
| `POST` | `/upload` | Uploads an image and returns the detected person count and processed image |

## 🔧 Technologies Used
- **Backend:** FastAPI, OpenCV, SQLAlchemy
- **Frontend:** Next.js, Tailwind CSS
- **Database:** PostgreSQL
- **Deployment:** Docker, Docker Compose


## 🎥 DEMO 


[output.webm](https://github.com/user-attachments/assets/731eedbc-1d45-4a24-afcf-33fdefa5e446)

---
🚀 **Enjoy using the Person Detection Web App!** 🎉

