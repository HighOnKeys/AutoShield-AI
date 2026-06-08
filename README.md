<div align="center">
# AutoShield AI

![Python](https://img.shields.io/badge/Python-3.10+-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-189AB4?style=for-the-badge)
[![Live Demo](https://img.shields.io/badge/Live-Demo-success?style=for-the-badge&logo=streamlit)](https://autoshield-ai.streamlit.app/)

*Automotive Supply Chain Risk Intelligence Platform*

</div>

## Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Solution Architecture](#solution-architecture)
- [Key Features](#key-features)
  - [🚨 Supply Chain War Room](#🚨-supply-chain-war-room)
  - [⚠️ Supplier Risk Explorer](#⚠️-supplier-risk-explorer)
  - [🔄 Alternative Sourcing Engine](#🔄-alternative-sourcing-engine)
  - [⚡ Scenario Simulator](#⚡-scenario-simulator)
  - [🤖 Executive AI Copilot](#🤖-executive-ai-copilot)
- [Machine Learning Pipeline](#machine-learning-pipeline)
- [Data Engineering Workflow](#data-engineering-workflow)
  - [Notebook 1](#notebook-1)
  - [Notebook 2](#notebook-2)
  - [Notebook 3](#notebook-3)
- [Technology Stack](#technology-stack)
  - [Data Science](#data-science)
  - [Visualization](#visualization)
  - [Supply Chain Analytics](#supply-chain-analytics)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Business Impact](#business-impact)
- [Future Enhancements](#future-enhancements)
- [Author](#author)

## Overview

Modern automotive supply chains operate across hundreds of suppliers, multiple geographies, and critical commodities such as semiconductors, battery materials, and mechanical assemblies.

Disruptions caused by supplier failures, logistics delays, material shortages, or geopolitical events can lead to production stoppages and significant financial losses.

AutoShield AI is an end-to-end supply chain risk intelligence platform that enables organizations to:

* Predict disruption risk using Machine Learning
* Monitor supplier and commodity risk exposure
* Identify alternative sourcing opportunities
* Simulate supply chain disruptions
* Support executive decision-making through an AI Copilot

The platform transforms raw supply chain data into actionable procurement intelligence.

---

## Problem Statement

Automotive manufacturers face increasing supply chain uncertainty due to:

* Semiconductor shortages
* Supplier failures
* Logistics disruptions
* Delivery delays
* Commodity constraints
* Geopolitical risks

Most organizations identify disruptions only after they occur.

The challenge is to proactively detect risks, quantify business impact, and recommend mitigation strategies before operations are affected.

---

## Solution Architecture

<img width="1145" height="1280" alt="architecture" src="https://github.com/user-attachments/assets/1a3431cf-06e4-44a2-8a5c-c843a73edd7f" />

---

## Key Features

### 🚨 Supply Chain War Room

Executive dashboard providing:

* Supply chain KPIs
* Supplier risk monitoring
* Commodity risk visibility
* Strategic insights

---

### ⚠️ Supplier Risk Explorer

Analyze supplier performance through:

* Risk scores
* Procurement readiness
* Commodity-level intelligence
* Risk segmentation

---

### 🔄 Alternative Sourcing Engine

Identify replacement suppliers using:

* Procurement Score
* Risk Profile
* Order Volume
* Revenue Contribution

---

### ⚡ Scenario Simulator

Simulate disruptions such as:

* Semiconductor shortages
* Supplier failures
* Commodity constraints

Outputs include:

* Revenue exposure
* Impacted orders
* Alternative sourcing recommendations
* Mitigation strategies

---

### 🤖 Executive AI Copilot

Natural language decision support system capable of answering:

* Which suppliers are highest risk?
* Which commodities are highest risk?
* Recommend alternative suppliers
* What happens if semiconductor supply fails?

---

## Machine Learning Pipeline

### Risk Prediction Model

Algorithm:

```text
XGBoost Classifier
```

Target Variable:

```text
Late_delivery_risk
```

Features:

* Days for shipping (real)
* Days for shipment (scheduled)
* Order Item Quantity
* Sales
* Order Region
* Order Country
* Shipping Mode

Performance:

| Metric   | Score  |
| -------- | ------ |
| Accuracy | 97.45% |
| ROC-AUC  | 97.57% |

---

## Data Engineering Workflow

### Notebook 1

```text
00_automotive_digital_twin.ipynb
```

Creates:

* Automotive Digital Twin
* Supplier Mapping
* Commodity Mapping
* Delay Features

---

### Notebook 2

```text
01_supplier_risk_agent.ipynb
```

Creates:

* XGBoost Risk Model
* Disruption Probabilities
* Risk Scores

---

### Notebook 3

```text
02_supplier_directory.ipynb
```

Creates:

* Supplier Intelligence Layer
* Procurement Scores
* Alternative Sourcing Logic
* Scenario Simulation Inputs

---

## Technology Stack

### Data Science

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost

### Visualization

* Streamlit
* Plotly

### Supply Chain Analytics

* Supplier Intelligence Modeling
* Procurement Readiness Scoring
* Scenario Simulation

---

## Project Structure

```text
AutoShield-AI/
│
├── data/
│   ├── processed/
│   │    └── automotive_digital_twin.csv
│   ├── final_supplier_directory.csv
│   └── risk_scored_supply_chain.csv
│   
├── docs/
│   ├── architecture.png
│   └── problem_definition.md
│
├── notebooks/
│   ├── 00_automotive_digital_twin.ipynb
│   ├── 01_supplier_risk_agent.ipynb
│   └── 02_supplier_directory.ipynb
│
├── pages/
│   ├── alternative_sourcing.py
│   ├── executive_copilot.py
│   ├── scenario_simulator.py
│   ├── supplier_risk.py
│   └── war_room.py
│
├── utils/
│   ├── __init__.py
│   ├── risk_engine.py
│   ├── sourcing_engine.py
│   └── simulation_engine.py
│
├── README.md
├── app.py
└── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd AutoShield-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Business Impact

AutoShield AI helps organizations:

* Detect supplier risks earlier
* Improve sourcing resilience
* Reduce disruption exposure
* Accelerate decision making
* Improve supply chain visibility

---

## Future Enhancements

* Real-time supply chain monitoring
* Live supplier intelligence feeds
* Commodity price forecasting
* GenAI-powered risk assessment
* Multi-tier supplier network analysis

---

# Author

**Kumar Manas**
B.Tech. Production and Industrial Engineering · IIT Roorkee

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kumarmanas-iitroorkee/)
[![GitHub](https://img.shields.io/badge/GitHub-121011?style=flat&logo=github&logoColor=white)](https://github.com/HighOnKeys)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat&logo=gmail&logoColor=white)](mailto:krmanas0811@gmail.com)

---

<div align="center">
<i>Built for ET AutoTech Hackathon 2026 · ET TechGig</i>
</div>
