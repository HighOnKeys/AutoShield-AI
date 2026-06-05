# 🚨 AutoShield AI: Automotive Supply Chain Risk Intelligence Platform

## Overview

AutoShield AI is an AI-powered supply chain risk intelligence platform designed for the automotive industry.

Modern automotive manufacturing depends on globally distributed suppliers for semiconductors, battery materials, mechanical assemblies, and other critical components. Supply disruptions can result in production delays, increased costs, and significant revenue loss.

AutoShield AI enables organizations to proactively identify supply chain risks, simulate disruptions, evaluate business impact, and recommend alternative sourcing strategies.

---

## Problem Statement

Automotive supply chains face increasing uncertainty due to:

* Supplier failures
* Logistics disruptions
* Material shortages
* Geopolitical risks
* Delivery delays

Most organizations react to disruptions after they occur.

AutoShield AI helps decision makers move from reactive supply chain management to proactive risk mitigation.

---

## Solution Architecture

<img width="1145" height="1280" alt="architecture" src="https://github.com/user-attachments/assets/1a3431cf-06e4-44a2-8a5c-c843a73edd7f" />

---

## Key Features

### 🚨 Supply Chain War Room

Executive dashboard providing:

* Supplier risk monitoring
* Commodity risk visibility
* Supply chain KPIs
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

├── app.py

├── data/

├── notebooks/
│   ├── 00_automotive_digital_twin.ipynb
│   ├── 01_supplier_risk_agent.ipynb
│   └── 02_supplier_directory.ipynb

├── pages/
│   ├── war_room.py
│   ├── supplier_risk.py
│   ├── alternative_sourcing.py
│   ├── scenario_simulator.py
│   └── executive_copilot.py

├── utils/
│   ├── risk_engine.py
│   ├── sourcing_engine.py
│   └── simulation_engine.py

└── README.md
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

## Authors

Developed as part of an Automotive AI & Supply Chain Intelligence Hackathon project.
"""
