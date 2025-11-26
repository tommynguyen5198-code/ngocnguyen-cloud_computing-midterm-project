# Cloud Computing midterm project
This project purpose for cloud computing midterm project

## Background:

A multi-container application with Flask backend and Nginx frontend using Docker Compose.

## Structure:

```
ngocnguyen-cloud_computing-midterm-project/
├── backend/
│   ├── app.py
│   └── Dockerfile
|   └── requirement.txt
├── frontend/
│   ├── index.html
│   └── nginx.conf
├── logs/
├── docker-compose.yml
└── README.md
```
## Requirements:
```
Docker
Docker compose
```
## Setup Instruction
### 1. Clone the repository:
```
git clone <your-repo-url>
cd ngocnguyen-cloud_computing-midterm-project
```
### 2. Build and run the containers:

```
docker compose up -d
```
### 3. Verify the application is running:

```
# Check frontend
curl "http://localhost:8089/"

# Check backend and create log entry
curl "http://localhost:8089/api/log"
```

### 4. Monitor logs in real-time:
```
tail -f logs/lha_access.log
```
## Clean up
To stop and remove all containers:
```
docker compose down
```
To clean images:
```
docker images | grep ngocnguyen | awk '{print $3}' | xargs docker rmi -f
```
