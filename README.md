# Quick-PDF 🚀

Quick-PDF is a fast, secure, and lightweight PDF merging web application built using modern backend and DevOps practices.  
It allows users to merge PDF files easily through a clean UI and download the merged file instantly.

This project is Dockerized, CI/CD enabled, and deployed on AWS EC2, making it production-ready and portfolio-worthy.

---

## 🌟 Features

- 📄 Merge two PDF files into a single PDF  
- ⚡ High-performance backend using FastAPI  
- 🎨 Modern, minimal, user-friendly UI  
- 🔐 Secure handling (temporary file storage only)  
- 🐳 Dockerized application  
- 🤖 Automated CI/CD using GitHub Actions  
- ☁️ Deployed on AWS EC2 (Production-ready)

---

## 🛠 Tech Stack

- Backend: FastAPI (Python)
- PDF Processing: PyPDF
- Frontend: HTML, CSS, JavaScript
- Containerization: Docker
- CI/CD: GitHub Actions
- Cloud: AWS EC2
- Server: Uvicorn

---

## 📂 Project Structure

Quick-PDF/
├── app/
│   ├── main.py
│   ├── routes/
│   │   └── merge.py
│   └── static/
│       └── index.html
├── requirements.txt
├── Dockerfile
├── .github/workflows/docker-build.yml
└── README.md

---

## 🚀 Running Locally

### Clone the repository
git clone https://github.com/rahman5828/Quick-PDF.git  
cd Quick-PDF

### Create virtual environment
python -m venv venv

Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

### Install dependencies
pip install -r requirements.txt

### Run the application
uvicorn app.main:app --reload

Open:
http://127.0.0.1:8000

---

## 🐳 Docker Usage

### Build image
docker build -t quick-pdf .

### Run container
docker run -d --name quick-pdf -p 80:8000 quick-pdf

---

## 🔄 CI/CD

GitHub Actions builds and pushes Docker images automatically on every push to main branch.

---

## ☁️ Production Deployment

- AWS EC2 (Ubuntu)
- Docker installed
- Port 80 opened in Security Group
- Container runs using Docker

---

## 👨‍💻 Author

Abdul Rahman  
GitHub: https://github.com/rahman5828

Built with ❤️ using FastAPI, Docker, AWS & DevOps best practices
