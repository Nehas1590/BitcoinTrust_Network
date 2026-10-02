# Bitcoin Alpha Web of Trust Network Analysis

A network visualization and analysis project based on the **Bitcoin Alpha Web of Trust Network**, developed using **Python, NetworkX, Matplotlib, and Streamlit**.

## 📌 Project Overview

This project analyzes the structure of the Bitcoin Alpha Web of Trust Network using network analysis techniques.

The dataset represents a **Web of Trust**, where users provide ratings to other users. The project focuses on understanding the structure and importance of users within the network through centrality measures and network-level measures.

> **Note:** This is a trust/rating network, not a Bitcoin financial transaction network.

## 🎯 Objectives

- Construct a network from the Bitcoin Alpha Web of Trust dataset.
- Visualize the network structure.
- Analyze degree centrality.
- Analyze closeness centrality.
- Analyze betweenness centrality.
- Calculate network transitivity.
- Calculate network reciprocity.
- Analyze degree assortativity.
- Present the results through an interactive Streamlit dashboard.

## 📊 Dataset

The project uses the **Bitcoin Alpha Web of Trust Network** dataset.

The dataset contains:

- **3,783 users (nodes)**
- **24,186 directed connections (edges)**
- User ratings ranging from **-10 to +10**
- Timestamp information for ratings

### Dataset Structure

| Column | Description |
|---|---|
| Source | User who gives the rating |
| Target | User who receives the rating |
| Rating | Rating assigned by the source user to the target user |
| Time | Timestamp indicating when the rating was recorded |

## 🛠️ Technologies Used

- Python
- Pandas
- NetworkX
- Matplotlib
- Streamlit
- Jupyter Notebook

## 🔬 Methodology

The analysis follows these main steps:

1. Load and inspect the dataset.
2. Check for missing values and duplicate source-target pairs.
3. Construct a directed network using NetworkX.
4. Visualize the top 50 connected users.
5. Calculate degree centrality.
6. Calculate closeness centrality.
7. Calculate betweenness centrality.
8. Calculate network transitivity.
9. Calculate network reciprocity.
10. Calculate degree assortativity.
11. Present the findings through a Streamlit dashboard.

## 📈 Key Results

| Measure | Result |
|---|---:|
| Number of Nodes | 3,783 |
| Number of Edges | 24,186 |
| Top Degree Centrality | User 1 (0.2348) |
| Top Closeness Centrality | User 2 (0.3668) |
| Top Betweenness Centrality | User 1 (0.1492) |
| Transitivity | 0.0780 |
| Reciprocity | 0.8321 |
| Degree Assortativity | -0.1635 |

Centrality values describe the position of users within the network structure; they do not directly represent the trustworthiness of a user.

## 🌐 Network Visualization

The project visualizes the **top 50 connected users** to make the network structure easier to interpret.

The complete network contains 3,783 users and 24,186 directed connections.

## 💻 Streamlit Dashboard

The project includes an interactive Streamlit dashboard with sections for:

- Overview
- Network Visualization
- Centrality Analysis
- Network-Level Measures
- Key Findings
- About the Dataset
- Download Analysis Results

## 📁 Project Structure

```text
BitcoinTrust_Network/
│
├── app/
│   └── app.py
│
├── dataset/
│   └── soc-sign-bitcoinalpha.csv
│
├── graphs/
│   ├── bitcoin_trust_network_top50.png
│   ├── network_level_measures.png
│   ├── top10_betweenness_centrality.png
│   ├── top10_closeness_centrality.png
│   └── top10_degree_centrality.png
│
├── results/
│   └── network_analysis_summary.csv
│
├── BitcoinTrust_Network_Analysis
├── requirements.txt
├── .gitignore
└── README.md