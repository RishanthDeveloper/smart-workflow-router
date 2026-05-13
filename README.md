# 🧠 Smart Workflow Router: Reinforcement Learning for Enterprise

![Python](https://img.shields.io/badge/Python-FastAPI-blue)
![Java](https://img.shields.io/badge/Java-Spring_Boot-green)
![React](https://img.shields.io/badge/React-Vite-61DAFB)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep_Q--Network-red)

## 📌 The Problem
Traditional business software uses static, rule-based routing (e.g., "If a ticket is about billing, send to the Accounting queue"). This fails to account for human variables: certain agents resolve specific types of problems faster than others, and agent proficiency changes over time. 

## 🚀 The Solution
This project replaces static IF/THEN rules with an AI-driven **Deep Q-Network (DQN)**. 
1. **The User** submits a support ticket via the React frontend.
2. **The Java Backend** receives the ticket and asks the AI who should handle it.
3. **The Python AI Engine** observes the ticket (Category, Urgency) and predicts the best human agent based on past performance.
4. **Reinforcement Learning:** When the ticket is resolved, the system calculates a "Reward" based on resolution speed. The AI continuously learns who is best at what, naturally optimizing the company's operational efficiency.

## 🏗️ Tech Stack
* **Frontend:** React.js, Tailwind CSS (User Dashboard)
* **Core Backend:** Java 17, Spring Boot (REST APIs, Workflow Management)
* **AI Engine:** Python, PyTorch, FastAPI (DQN Algorithm)

## ⚙️ How to Run Locally

### 1. Start the AI Engine (Python)
Navigate to the `rl-engine` folder, install the dependencies, and start the FastAPI server:
```bash
cd rl-engine
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
