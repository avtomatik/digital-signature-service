# 🧾 Digital Signature Service (Toy Project)

> **Mock implementation** of a trusted digital signature platform for educational and testing purposes.
> Built with **Python 3.12**, **PostgreSQL**, **RabbitMQ**, and **Redis**.
> ⚠️ *This project is for demonstration only — no real cryptographic operations are performed.*

---

## 📖 Overview

This project imitates a **qualified digital signature service**, capable of:

* Receiving signing requests from clients (e.g., documents or payloads).
* Simulating signature generation and returning valid-like responses.
* Publishing and consuming service events via **RabbitMQ**.
* Storing request/response metadata in **PostgreSQL**.
* Utilizing **Redis** for temporary data caching or request throttling.

The focus is on **system integration, asynchronous design**, and **load testing**, not on real-world cryptography.

---

## 🧩 Components

| Component                           | Description                                                |
| ----------------------------------- | ---------------------------------------------------------- |
| **Backend (FastAPI)**               | Core API service handling signature requests and responses |
| **PostgreSQL**                      | Persistent data storage                                    |
| **RabbitMQ**                        | Event bus for asynchronous message passing                 |
| **Redis**                           | In-memory cache layer                                      |
| **Frontend (optional)**             | Minimal page or SPA for interacting with backend           |
| **Locust Tests (external project)** | Load and performance testing tool                          |

---

## 🏗 Architecture Diagram (Conceptual)

```
   ┌─────────────┐       ┌──────────────┐
   │  Frontend   │──────▶️│   Backend    │──┐
   └─────────────┘       └──────────────┘  │
                                            │
        ┌───────────────┬──────────────────┼────────────────┐
        │               │                  │                │
   ┌────────┐      ┌────────────┐      ┌────────┐      ┌────────────┐
   │ Postgres│◀️──▶️│   RabbitMQ │◀️──▶️│ Redis  │◀️──▶️│ Locust Tests│
   └────────┘      └────────────┘      └────────┘      └────────────┘
```

---

## ⚙️ Setup & Development

### Prerequisites

* Python **3.12+**
* Docker & Docker Compose
* (optional) Node.js — if developing frontend

### Run via Docker Compose

```bash
cd digital-signature-service
docker-compose up
```

This launches:

* Backend (FastAPI)
* PostgreSQL (port 5432)
* RabbitMQ (ports 5672, 15672)
* Redis (port 6379)

Access the backend at [http://localhost:8000](http://localhost:8000).

---

## 🧪 Testing

For load testing, use the separate **`locust-tests/`** project:

```bash
cd ../locust-tests
locust -f locustfile.py --host=http://localhost:8000
```

Locust web UI: [http://localhost:8089](http://localhost:8089)

---

## 🧱 Project Structure

```
digital-signature-service/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   └── services/
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   └── package.json
├── docker-compose.yml
├── docker-compose.override.yml  # Optional: integrated Locust setup
└── README.md
```

---

## 🚧 Roadmap / TODO

* [ ] Implement FastAPI backend with stub `/sign` endpoint
* [ ] Integrate PostgreSQL ORM (SQLAlchemy or Tortoise)
* [ ] Add RabbitMQ producer/consumer for simulated event flow
* [ ] Add Redis caching layer
* [ ] Provide OpenAPI documentation via FastAPI
* [ ] Add minimal HTML/SPA frontend (optional)
* [ ] Add Docker Compose for local development
* [ ] Connect to Locust load tests
* [ ] Write basic unit tests

---

## 🧠 Notes

* The service imitates **response timing, data persistence**, and **asynchronous processing**, but does **not** perform real cryptographic signing.
* All sensitive operations are **mocked** or **simulated** for testing.

---

## 📜 License

MIT License © 2025 — Created for educational and research purposes.
