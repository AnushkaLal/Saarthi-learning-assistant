# Backend Foundation - Saarthi Learning Assistant

## Structure

```
backend/
├── app/
│   ├── __init__.py
│   └── main.py
├── api/
│   ├── __init__.py
│   ├── routes.py
│   ├── upload.py
│   └── analyze.py
├── services/
│   ├── __init__.py
│   └── document_service.py
├── models/
│   ├── __init__.py
│   └── schemas.py
├── db/
│   ├── __init__.py
│   └── database.py
├── core/
│   ├── __init__.py
│   ├── config.py
│   ├── logger.py
│   └── exceptions.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── main.py
```

## To Run

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```
