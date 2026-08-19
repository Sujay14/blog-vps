# Fast Blog API

A simple blog application built with **FastAPI, PostgreSQL, SQLAlchemy and JWT Authentication**.

## Features

* User authentication
* Create, update and delete posts
* User profiles
* Password reset
* Profile picture upload
* PostgreSQL database
* AWS S3 storage
* Jinja2 templates

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* Pydantic
* JWT
* AWS S3
* Jinja2

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Sujay14/fast_blog_api.git
cd fast_blog_api
```

### 2. Install dependencies

This project uses `uv`.

```bash
uv sync
```

### 3. Configure environment variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key

S3_BUCKET_NAME=your_bucket
S3_REGION=your_region
S3_ACCESS_KEY_ID=your_access_key
S3_SECRET_ACCESS_KEY=your_secret_key
```

Add your email configuration if you want to use the password reset feature.

### 4. Run migrations

```bash
uv run alembic upgrade head
```

### 5. Start the server

```bash
uv run uvicorn main:app --reload
```
or
```bash
uv run fastapi dev main.py
```

The application will be available at:

```text
http://localhost:8000
```

## API Documentation

Once the server is running:

```text
http://localhost:8000/docs
```

or

```text
http://localhost:8000/redoc
```

## Project Structure

```text
fast_blog_api/
├── routers/
├── templates/
├── static/
├── alembic/
├── main.py
├── models.py
├── schemas.py
├── database.py
├── auth.py
└── config.py
```

## Author

**Sujay**

GitHub: https://github.com/Sujay14 hi
