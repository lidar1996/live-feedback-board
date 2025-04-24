# Live Feedback Board
**Live Feedback Board** is a Full Stack microservices-based project that enables real-time, anonymous feedback submission.

<img src="https://github.com/user-attachments/assets/18e8a813-f620-4134-b36b-2220a947b9d3" alt="Live Feedback Board Screenshot" width="600"/>

## Project Structure

- `auth-service` – Handles authentication and user identification (JWT-based).
- `feedback-service` – Manages feedback storage and logic.
- `websocket-service` – Provides real-time WebSocket communication.
- `frontend` – React-based web interface.
- `shared` – Shared configurations and models used by all services.

---

## Local Development Setup

### Prerequisites

- Node.js 18+
- Python 3.10+
- Docker & Docker Compose
- `pipenv` or `virtualenv` for Python environments
- `npm` or `yarn` for the frontend

---

### Step 1: Start External Services

```bash
docker-compose up -d
```

This will spin up:
- Redis (localhost:6379)
- PostgreSQL (localhost:5432)
- Kafka (localhost:9092)
- Zookeeper (localhost:2181)

### Step 2: Environment Variables
Each service (e.g., auth-service, feedback-service, websocket-service) requires a .env file in its root directory with the necessary configuration.

Example .env file for auth-service:
```bash
JWT_SECRET=123
JWT_EXP_MINUTES=60
REDIS_URL=redis://localhost:6379/0
DATABASE_URL=postgresql://user:password@localhost:5432/mydb
```

### Step 3: Run Services
Each service must be run individually. For example:
```bash
cd auth-service
pipenv install
pipenv run python app.py
```
Repeat for other services (feedback-service, websocket-service, etc.).

### Step 4: Run the Frontend
```bash
cd frontend
npm install
npm start
```
The app will be available at: http://localhost:3000

### TODO / Coming Soon
- Kubernetes deployment (Helm charts, manifests, etc.)
- CI/CD pipeline with automated Docker image pushes
- Unit and integration testing
- Advanced user management features
