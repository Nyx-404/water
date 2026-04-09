# 💧 Rainwater Harvesting Decision Support System

## 📌 Overview
This project is a **Predictive Decision Support System (DSS)** that analyzes rainfall data and simulates rainwater harvesting to help users evaluate water availability and sustainability.

It provides both:
- **Analytical insights** using Power BI
- **Interactive predictions** using a Streamlit web application

---

## 🚀 Features
- Rainwater harvesting calculation
- Monthly storage simulation
- Shortage and overflow detection
- Sustainability analysis
- Interactive user input (Streamlit)
- Data visualization dashboard (Power BI)

---

## 🧠 Methodology
The system uses a **water balance model**:

Storage = Previous Storage + Harvested Water − Demand

Constraints:
- Storage cannot exceed tank capacity
- Storage cannot go below zero

This allows simulation of real-world water usage scenarios.

---

## 🛠️ Technologies Used
- Python (Streamlit)
- Power BI
- Data Analysis

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install streamlit pandas
