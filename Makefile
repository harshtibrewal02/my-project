.PHONY: run test deploy clean install

install:
	pip install -r requirements.txt

run:
	venv\Scripts\uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

test:
	venv\Scripts\python -m pytest tests/ -v

deploy:
	docker-compose up --build

clean:
	docker-compose down
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
