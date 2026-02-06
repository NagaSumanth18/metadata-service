# Metadata Service API

A simple Metadata Service built using **FastAPI**, **MySQL**, **SQLAlchemy**, and **Alembic**.  
The service allows managing datasets, their columns, lineage relationships, and searching datasets by name.

---

## 🚀 Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy ORM
- Alembic (database migrations)
- MySQL 8
- Docker & Docker Compose

---

## 📦 Features

- Create and list datasets
- Store dataset columns
- Maintain dataset lineage (upstream → downstream)
- Search datasets using partial name match
- Fully Dockerized setup

---

## 🛠️ How to Run the Project

### Prerequisites
- Docker
- Docker Compose

### Steps

1. Clone the repository or unzip the project folder  

2. Navigate to the project root (where `docker-compose.yml` exists)

3. Start the services using Docker Compose:
```bash
docker compose up --build
Wait until the following services are running:

FastAPI application

MySQL database

Apply database migrations:

docker exec -it metadata_api alembic upgrade head
Open the API in your browser:

Health check: http://localhost:8000/

Swagger UI: http://localhost:8000/docs

Test the APIs using Swagger UI or Postman:

Create datasets

Add dataset columns

Define dataset lineage

Search datasets

To stop the services:

docker compose down


## 🔐 Environment Variables

The project uses a `.env` file for database configuration.

Sample values are already provided for ease of setup:

```env
DB_USER=metadata_user
DB_PASSWORD=metadata_pass
DB_HOST=db
DB_PORT=3306
DB_NAME=metadata_db
