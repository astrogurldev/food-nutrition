# 🍽️ Food Nutrition Analyzer — MLOps with Kubernetes

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

> A production-grade MLOps project that detects food from images and provides detailed nutrition information with diet recommendations — deployed with Docker, Kubernetes, and CI/CD pipeline.

[![CI/CD Pipeline](https://github.com/astrogurldev/food-nutrition/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/astrogurldev/food-nutrition/actions/workflows/ci-cd.yml)

---

## 🎯 Project Overview

This project deploys a **food classification ML model** (ViT fine-tuned on Food-101) as a containerized microservice. Users upload a food photo and instantly get:

- 🍕 **Food identification** (101 types of food)
- 📊 **Nutrition info** (calories, protein, carbs, fat per 100g)
- 🥗 **Diet label** (Diet Friendly / Moderate / Hindari)
- 💡 **Diet recommendations** in Bahasa Indonesia

🌐 **Live Demo:** https://astrogurldev-food-nutrition.hf.space

---

## 🏗️ Architecture

```
Developer pushes code
        ↓
GitHub Actions (CI/CD)
        ↓
┌───────────────────────────────────┐
│  Test → Build Docker → Deploy     │
└───────────────────────────────────┘
        ↓
Docker Hub (Image Registry)
        ↓
Kubernetes Cluster (Minikube)
        ↓
┌─────────┐  ┌─────────┐  ┌─────────┐
│  Pod 1  │  │  Pod 2  │  │  Pod N  │  ← Auto-scaled by HPA
│ [Flask] │  │ [Flask] │  │ [Flask] │
│ [ViT]   │  │ [ViT]   │  │ [ViT]   │
└─────────┘  └─────────┘  └─────────┘
```

---

## ✨ Key Features

- 🤖 **ML Model**: ViT fine-tuned on Food-101 (101 food classes, 101K images)
- 🐳 **Dockerized**: Fully containerized with optimized multi-layer caching
- ☸️ **Kubernetes**: Deployed with Deployment, Service, and HPA
- 📈 **Auto-Scaling**: HPA scales pods from 2 → 10 based on CPU usage
- 🔄 **CI/CD Pipeline**: GitHub Actions — auto test, build, push, deploy on every push
- 🥗 **Diet Intelligence**: Nutrition database with personalized diet recommendations

---

## 🍽️ Supported Foods (Sample)

| Food | Calories | Diet Label |
|---|---|---|
| Salad | 20 kcal | ✅ Diet Friendly |
| Grilled Salmon | 208 kcal | ✅ Diet Friendly |
| Sushi | 143 kcal | ✅ Diet Friendly |
| Fried Rice | 163 kcal | ⚠️ Moderate |
| Pizza | 266 kcal | ⚠️ Moderate |
| French Fries | 312 kcal | ❌ Hindari |
| Ice Cream | 207 kcal | ❌ Hindari |

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| **ML Model** | ViT (Vision Transformer), HuggingFace Transformers |
| **Dataset** | Food-101 (101K images, 101 classes) |
| **Backend** | Python, Flask |
| **Containerization** | Docker, Docker Hub |
| **Orchestration** | Kubernetes, Minikube |
| **Auto-Scaling** | Horizontal Pod Autoscaler (HPA) |
| **CI/CD** | GitHub Actions |
| **Deployment** | HuggingFace Spaces |

---

## 🚀 Quick Start

### Prerequisites
- Docker Desktop
- Minikube
- kubectl
- Python 3.11+

### 1. Clone Repository
```bash
git clone https://github.com/astrogurldev/food-nutrition.git
cd food-nutrition
```

### 2. Build & Push Docker Image
```bash
docker build -f docker/Dockerfile -t astrogurldev/food-nutrition:v1 .
docker push astrogurldev/food-nutrition:v1
```

### 3. Deploy to Kubernetes
```bash
minikube start
minikube addons enable metrics-server
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml
```

### 4. Access the App
```bash
kubectl port-forward service/food-nutrition-service 8080:80
```
Open: http://localhost:8080

---

## 📊 Auto-Scaling Demo

```bash
kubectl get pods -w
kubectl get hpa
```

When traffic increases, Kubernetes automatically adds new pods:
```
REPLICAS: 4  ← Scaled up automatically from 2!
```

---

## 📁 Project Structure

```
food-nutrition/
├── .github/
│   └── workflows/
│       └── ci-cd.yml           # GitHub Actions CI/CD
├── app/
│   ├── app.py                  # Flask API + ML model
│   ├── nutrition_data.py       # Nutrition database
│   ├── requirements.txt        # Python dependencies
│   └── templates/
│       └── index.html          # Web UI
├── docker/
│   └── Dockerfile              # Docker image
├── k8s/
│   ├── deployment.yaml         # Kubernetes Deployment
│   ├── service.yaml            # Kubernetes Service
│   └── hpa.yaml                # Horizontal Pod Autoscaler
└── README.md
```

---

## 🔗 Links

- 🌐 **Live App:** https://astrogurldev-food-nutrition.hf.space
- 🐳 **Docker Hub:** https://hub.docker.com/r/astrogurldev/food-nutrition
- ⚙️ **CI/CD Pipeline:** https://github.com/astrogurldev/food-nutrition/actions

---

## 🤝 Connect

**Aisha** — DevOps Engineer
- GitHub: [@astrogurldev](https://github.com/astrogurldev)
- Docker Hub: [astrogurldev](https://hub.docker.com/u/astrogurldev)