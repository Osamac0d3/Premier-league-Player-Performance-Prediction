# ⚽ Player Performance Prediction Web App

A **Machine Learning + Flask web application** that predicts and displays the **Top football players for a match** based on predicted performance ratings.
Users can select a **team** and an **opponent team**, and the system returns the **best players ranked by predicted rating** along with **visual analytics dashboards**.

---

## 🚀 Project Overview

This project uses **historical Premier League player data** to build a prediction system that estimates **player performance ratings** for a specific match.

The web application allows users to:

* Select two teams
* Predict the **top 30 players** likely to perform best
* View **interactive visualizations** of player statistics
* Analyze player performance using **data-driven insights**

---

## 🧠 Machine Learning Workflow

1. **Data Collection**

   * Premier League player data from the last **5 years**

2. **Data Preprocessing**

   * Cleaning missing values
   * Feature selection
   * Encoding categorical features

3. **Feature Engineering**

   * Player match statistics
   * Goals
   * Assists
   * Shots
   * Passes completed
   * Tackles
   * Minutes played

4. **Model Training**

   * Model predicts **player rating**
   * Used to rank players by performance

5. **Deployment**

   * Flask web application
   * Interactive charts using Chart.js

---

## 🖥️ Web Application Features

### 🔎 Team vs Team Prediction

Users select:

* Team
* Opponent Team

The system displays the **Top 30 predicted players**.

---

### 📊 Data Visualization Dashboard

The results page includes interactive charts such as:

* Player Goals Distribution
* Assists Comparison
* Minutes Played Analysis

---

### 📋 Player Ranking Table

The system ranks players by **predicted performance rating**.

| Rank | Player Name | Team   |
| ---- | ----------- | ------ |
| 1    | Player A    | Team A |
| 2    | Player B    | Team B |
| 3    | Player C    | Team A |

---

## 🏗️ Project Structure

```
Player-Performance-Prediction/
│
├── app.py
├── player_data.pkl
├── premier_league_players_5years_with_rating.csv
├── Player_Performance_Prediction.ipynb
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/Player-Performance-Prediction.git
cd Player-Performance-Prediction
```

---

### 2️⃣ Install Dependencies

```bash
pip install flask pandas numpy scikit-learn
```

---

### 3️⃣ Run the Application

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 📊 Dataset

Dataset used in this project:

**Premier League Player Performance Dataset (5 Years)**

Contains features such as:

* Player name
* Team
* Opponent team
* Goals
* Assists
* Shots
* Passes completed
* Tackles
* Minutes played
* Match rating

---

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **HTML**
* **CSS**
* **Chart.js**

---

## 🎯 Future Improvements

* Player **Radar Charts**
* **Top 11 lineup prediction**
* **Team win probability prediction**
* **Deep Learning models**
* Full **Football Analytics Dashboard**

---

## 👨‍💻 Author

**Mohd Osama**

GitHub: https://github.com/Osamac0d3

---

## ⭐ If you like this project

Give it a **star on GitHub** ⭐ and feel free to contribute!
