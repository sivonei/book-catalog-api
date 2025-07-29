# Book Catalog API – Capstone Project

This is the Capstone Project for the DevOps Diploma at CCT College Dublin.
The goal is to build a backend application using Django and modern DevOps practices: containerization, CI/CD, and deployment with Kubernetes.

---

## Project Overview

The application is a **RESTful API to manage a book catalog**.
You can list, add, update, and delete books easily.

Main technologies used:

* **Python + Django REST Framework** for the API
* **Docker** for packaging the application
* **GitHub Actions** for the CI/CD pipeline
* **GitHub Container Registry (GHCR)** to store the Docker image
* **Helm + Kubernetes (Minikube)** for deployment

---

## Environment Used

* macOS (Intel Chip)
* Docker: `Docker version 20.10.21, build baeda1f`
* Kubernetes (Minikube):
  `Client Version: v1.25.2`
  `Kustomize Version: v4.5.7`

---

## Running Locally with Docker Compose

1. Clone the repository:

```bash
git clone https://github.com/sivonei/book-catalog-api.git
cd book-catalog-api
```

2. Start the application:

```bash
docker-compose up --build
```

3. Open your browser and access:

[http://localhost:8000/api/books/](http://localhost:8000/api/books/)

---

## Running Tests

Run unit tests using:

```bash
docker-compose exec web python manage.py test
```

There are at least 3 tests covering key functionality.

---

## Docker

The application image is available at GitHub Container Registry:

```bash
docker pull ghcr.io/sivonei/book-catalog-api:latest
```

---

## CI/CD with GitHub Actions

The CI/CD pipeline runs automatically on every push to the `main` branch. It performs:

1. Install dependencies
2. Run unit tests
3. Build Docker image
4. Push image to GHCR

This ensures the code is always tested and ready for deployment.

---

## Deployment with Kubernetes and Helm

### Step 1: Start Minikube cluster

```bash
minikube start
```

### Step 2: Deploy PostgreSQL

```bash
kubectl apply -f k8s/postgres-deployment.yaml
kubectl apply -f k8s/postgres-service.yaml
```

### Step 3: Deploy Book Catalog API using Helm

```bash
helm upgrade --install book-api ./book-catalog
```

### Step 4: Access the application

```bash
minikube service book-api
```

Or get the URL:

```bash
minikube service book-api --url
```

---

## Available API Endpoints

* `GET /api/books/` -> List all books
* `POST /api/books/` -> Add a new book
* `GET /api/books/{id}/` -> View book details
* `PUT /api/books/{id}/` -> Update a book
* `DELETE /api/books/{id}/` -> Delete a book

---

## Project Structure

```
book-catalog-api/          # Project root
├── .github/workflows/     # GitHub Actions workflows (CI/CD)
│
├── .venv/                # Python virtual environment (local, in .gitignore)
│
├── api/                  # Django REST API app
│
├── bookcatalog/          # Django project core
│
├── book-catalog/         # Helm chart
│
├── k8s/                  # Kubernetes manifests
|    
├── .env.example          # Environment template
├── .gitignore            # Includes .venv and db.sqlite3
├── docker-compose.yml    # Compose file for local development
├── Dockerfile            # Image build instructions
├── manage.py             # Django management
├── README.md             # Project documentation
└── requirements.txt      # Dependencies

```

---

## Author

**Sivonei dos Santos**

* LinkedIn: [linkedin.com/in/sivonei-ribeiro-00014078](https://www.linkedin.com/in/sivonei-ribeiro-00014078/)
* GitHub: [github.com/sivonei](https://github.com/sivonei)

---
