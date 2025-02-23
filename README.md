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
│   │   ├── ...
│   ├── requirements.txt
│   ├── Dockerfile
├── frontend/
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
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


[output.webm](https://github.com/user-attachments/assets/d0ccbe58-8412-46cd-b14e-bf357c725ffd)


---
🚀 **Enjoy using the Person Detection Web App!** 🎉

