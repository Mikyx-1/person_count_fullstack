# Person Counter Web App

## 📌 Overview
This is a **Person Counter Web Application** that allows users to upload an image, detect the number of people present, and visualise the detected bounding boxes. The results, including the processed image and count, are stored in a **PostgreSQL database**. The application consists of a **FastAPI** backend and a **Next.js** frontend, deployed using **Docker Compose**.

![Screenshot from 2025-02-26 00-15-46](https://github.com/user-attachments/assets/9feaf1f7-2e0b-49fb-9268-d497a8fed579)


## 🏗️ Architecture

The application follows a **client-server architecture**:

- **Frontend:** Built with Next.js to provide a user-friendly interface for uploading images and displaying detection results.
- **Backend:** Built with FastAPI, handling image processing and database operations.
- **Database:** PostgreSQL with SQLAlchemy for storing detection results.
- **Deployment:** Docker Compose for easy containerised deployment.

## ✨ Features

The application provides a robust set of features for counting person and result management:

- **Person Count:** Upload an image, and the system detects and counts the number of people in the image. A bounding box is drawn around each detected person, and the final count is displayed along with the processed image.

- **View Database:** A dedicated history page allows users to view all previous detection results, including the timestamp, number of people detected, and the path to the processed image.

- **Filter by Result Image Path:** Users can search and filter records based on the file path of the processed images, allowing quick access to specific images stored in the system.

- **Filter by Date:** Users can filter the history records by selecting a specific date range, making it easy to find detection results within a given timeframe.

- **Filter by Number of People:** Users can filter results based on the number of people detected, specifying a minimum and/or maximum count for more focused searches.

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

### 2️⃣ Clone the Repository
```sh
git clone https://github.com/Mikyx-1/person_count_fullstack.git
cd person-detection-app
```

### 3️⃣ Setup Environment Variables
Create a `.env` file in the root directory and configure it with database details:
```sh
# .env
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=mydb
TZ=Asia/Ho_Chi_Minh

# pgAdmin
PGADMIN_DEFAULT_EMAIL=admin@test.com
PGADMIN_DEFAULT_PASSWORD=admin

```

### 4️⃣ Run with Docker (Recommended)
```sh
docker-compose up --build
```
This will start the **backend, frontend, database**, and **pgAdmin** services.

### 5️⃣ Access the Application
- **Frontend UI**: [http://localhost:3000](http://localhost:3000)
- **Backend API Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **pgAdmin**: [http://localhost:5050](http://localhost:5050)

### 6️⃣ pgAdmin Setup
- **Login Credentials:**
  - **Email:** `admin@test.com`
  - **Password:** `admin`
- **Add New Server:**
  - **Name:** `person-detection-db`
  - **Host:** `db`
  - **Port:** `5432`
  - **Username:** `user`
  - **Password:** `password`

Once connected, you can browse the database and inspect tables and data.



## 📂 Folder Structure
```
PERSON_COUNT_FULLSTACK/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── endpoints.py
│   │   ├── ...
│   ├── requirements.txt
│   ├── Dockerfile
├── frontend/
│   ├── app/
│   │   ├── history/  # For history records web page
│   │   │   ├── page.tsx
│   │   ├── layout.tsx
│   │   ├── page.tsx  # Main page
│   ├── components/
│   │   ├── ui/
│   │   │   ├── fileUpload.tsx
│   │   │   ├── imageDisplay.tsx
│   ├── node_modules/
│   ├── public/
│   ├── Dockerfile
├── .gitignore
├── .env
├── docker-compose.yml
└── README.md
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

[output.webm](https://github.com/user-attachments/assets/e0ad5d95-26ae-41a8-bd01-a800bf275fe0)


---
🚀 **Enjoy using the Person Detection Web App!** 🎉

