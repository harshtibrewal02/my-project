# 🚀 My FastAPI Project — One-Click Deployment

![CI Pipeline](https://github.com/harshtibrewal02/my-project/actions/workflows/ci.yml/badge.svg?branch=dev)

A production-ready **FastAPI** application with a complete DevOps pipeline — automated testing, Docker containerization, and one-click deployment.

---

## ✨ Features

- ⚡ **FastAPI** with auto-generated Swagger docs (`/docs`)
- 🐳 **Docker + Docker Compose** for containerized deployment
- 🤖 **GitHub Actions CI** — tests run automatically on every push
- 🌍 **Multi-environment config** via `.env` files
- 📊 **Live health endpoint** with version and uptime

---

## 🔗 API Endpoints

| Method | Endpoint         | Description              |
|--------|------------------|--------------------------|
| GET    | `/`              | App status + environment |
| GET    | `/api/v1/health` | Health check + uptime    |
| GET    | `/docs`          | Interactive Swagger UI   |

---

## 🛠️ One-Click Commands

```bash
make install    # Install dependencies
make run        # Start dev server (hot reload)
make test       # Run all tests
make deploy     # Build & run with Docker
make clean      # Tear down Docker containers
```

---

## 🚀 Quick Start

### Local Development
```bash
git clone https://github.com/harshtibrewal02/my-project.git
cd my-project
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
make run
```
Visit: **http://localhost:8000/docs**

### Docker (One-Click Deploy)
```bash
make deploy
```
Visit: **http://localhost:8000**

---

## 🔧 Environment Variables

Copy `.env.example` to `.env` and configure:

```env
APP_NAME=My FastAPI Project
APP_VERSION=1.0.0
ENVIRONMENT=development     # development | staging | production
```

---

## 🧪 Running Tests

```bash
make test
```

---

## 📁 Project Structure

```
my-project/
├── app/
│   ├── main.py        # FastAPI app entry point
│   ├── routes.py      # API route handlers
│   └── config.py      # Environment config loader
├── tests/
│   └── test_main.py   # Automated tests
├── .github/workflows/
│   └── ci.yml         # GitHub Actions CI pipeline
├── Dockerfile         # Container definition
├── docker-compose.yml # One-click deployment
├── Makefile           # Shortcut commands
└── requirements.txt   # Python dependencies
```

---

## 🏗️ CI/CD Pipeline

```
git push → GitHub Actions → pytest → ✅ Pass → Docker Build → Deploy
```

Every push to `dev`, `stage`, or `main` automatically runs the test suite.
