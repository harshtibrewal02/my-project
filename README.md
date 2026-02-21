# 🚀 One-Click Deployment Template

![CI/CD Pipeline](https://github.com/harshtibrewal02/my-project/actions/workflows/ci.yml/badge.svg?branch=dev)

A **production-ready CI/CD template** for any Python project. Fork it, add 6 secrets, push — your app is live with automated testing, Docker builds, and rollback.

---

## ✨ What This Does

```
git push
    ↓
🧪 flake8 lint → mypy type check → pytest
    ↓  (pass)
🐳 Docker build → SHA tag → push to Docker Hub
    ↓  (main/stage only)
🚀 Deploy to Render → health check
    → ❌ fail → auto rollback to last stable version
    → ✅ pass → live!
```

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | App status + environment |
| GET | `/api/v1/health` | Health + version + uptime |
| GET | `/docs` | Interactive Swagger UI |

---

## ⚡ Use This As A Template (Any Project)

### Step 1 — Fork / Use Template
Click **"Use this template"** on GitHub → create your repo.

### Step 2 — Add 6 GitHub Secrets
Go to your repo → **Settings → Secrets → Actions → New secret**:

| Secret | Where to get it |
|--------|-----------------|
| `DOCKERHUB_USERNAME` | Your Docker Hub username |
| `DOCKERHUB_TOKEN` | Docker Hub → Account → Security → New Token |
| `RENDER_DEPLOY_HOOK_URL` | Render → Service → Settings → Deploy Hook |
| `RENDER_APP_URL` | e.g. `https://your-app.onrender.com` |
| `RENDER_API_KEY` | Render → Account Settings → API Key |
| `RENDER_SERVICE_ID` | Render → Service URL (e.g. `srv-xxxx`) |

### Step 3 — Push
```bash
git push origin main
```
**That's it.** Pipeline runs, app deploys, health check confirms. 🎉

---

## 🛠️ Local Development

```bash
git clone https://github.com/harshtibrewal02/my-project.git
cd my-project
python -m venv venv
venv\Scripts\activate       # Windows
pip install -r requirements.txt
```

## 🖥️ Makefile Commands

```bash
make run      # Start dev server with hot reload
make test     # Run lint + type check + tests
make deploy   # One-click Docker deploy locally
make clean    # Tear down containers
```

## 🐳 Docker

```bash
# Local build
docker-compose up --build

# Pull from Docker Hub (production)
DOCKER_IMAGE=youruser/your-repo:latest docker-compose up
```

---

## 📁 Project Structure

```
my-project/
├── app/
│   ├── main.py        # FastAPI app + config
│   ├── routes.py      # API endpoints
│   └── config.py      # Env var loader
├── tests/
│   └── test_main.py   # Automated tests
├── .github/workflows/
│   └── ci.yml         # Full CI/CD pipeline
├── Dockerfile         # Container build
├── docker-compose.yml # One-click local deploy
├── Makefile           # Dev shortcuts
├── .flake8            # Linting rules
├── mypy.ini           # Type checking config
└── requirements.txt   # Pinned dependencies
```

---

## 🔐 Environment Variables

Copy `.env.example` → `.env`:

```env
APP_NAME=My FastAPI Project
APP_VERSION=1.0.0
ENVIRONMENT=development   # development | staging | production
```
