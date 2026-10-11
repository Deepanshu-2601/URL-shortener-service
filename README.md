# 🔗 URL Shortener & Analytics API

A lightweight, production-ready URL shortener built with FastAPI, SQLAlchemy, and Pydantic. It generates short codes, redirects users to the original destination, and tracks click analytics in a SQLite database.

## Overview

This service allows you to:

- shorten long URLs into compact short links
- redirect short URLs to their original destination
- count how many times each short URL is opened
- store URL records using SQLite and SQLAlchemy
- explore the API automatically through Swagger UI and ReDoc

---

## Features

- Short URL generation using a unique 6-character alphanumeric code
- Instant HTTP 307 redirect to the original URL
- Click tracking and analytics per short URL
- Persistent storage with SQLite
- FastAPI-based REST API with automatic schema validation
- Interactive API documentation at `/docs` and `/redoc`

---

## Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Pydantic v2

---

## Project Structure

```text
URL-shortener-service/
├── .gitignore
├── README.md
├── __init__.py
├── crud.py
├── database.py
├── main.py
├── models.py
├── requirements.txt
├── schemas.py
├── url_shortener.db
├── utils.py
└── .venv/                  # optional local virtual environment
```

---

## Prerequisites

Before running the project, make sure you have:

- Python 3.10 or later
- pip installed
- a terminal or command prompt

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Deepanshu-2601/URL-shortener-service.git
cd URL-shortener-service
```

2. Create and activate a virtual environment:

### Linux / macOS
```bash
python -m venv .venv
source .venv/bin/activate
```

### Windows PowerShell
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The app will be available at:

- Swagger UI: http://127.0.0.1:8000/docs
- GitHub RE:  https://github.com/Deepanshu-2601/URL-shortener-service.git
---

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/` | Health check |
| POST | `/shorten` | Create a short URL |
| GET | `/{short_code}` | Redirect to the original URL |
| GET | `/analytics/{short_code}` | View URL analytics |

---

## Example Usage

### 1) Create a short URL

```bash
curl -X POST "http://127.0.0.1:8000/shorten" \
  -H "Content-Type: application/json" \
  -d '{"original_url": "https://example.com"}'
```

Example response:

```json
{
  "original_url": "https://example.com",
  "short_code": "aX9m2Q",
  "short_url": "http://127.0.0.1:8000/aX9m2Q",
  "clicks": 0,
  "created_at": "2026-10-11T12:00:00"
}
```

### 2) Open the short URL

```bash
curl -L "http://127.0.0.1:8000/aX9m2Q"
```

This will redirect to the original URL using HTTP 307.

### 3) Check analytics

```bash
curl "http://127.0.0.1:8000/analytics/aX9m2Q"
```

Example response:

```json
{
  "original_url": "https://example.com",
  "short_code": "aX9m2Q",
  "clicks": 1,
  "created_at": "2026-10-11T12:00:00"
}
```

---

## Database

The project uses SQLite, and the database file is created automatically as:

```text
url_shortener.db
```

The application stores the following fields:

- `id`
- `original_url`
- `short_code`
- `clicks`
- `created_at`

---

## Notes

- The project automatically creates database tables when the app starts.
- The generated short code is a random 6-character alphanumeric string.
- Click tracking is incremented every time the short URL is accessed.

---

## License

This project is provided for learning and development purposes.

If you want, I can also rewrite the README into a more professional GitHub-style version with badges, screenshots, and a cleaner project summary.
