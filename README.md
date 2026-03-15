# ⚽ Player Performance Prediction using Deep Learning

A **Deep Learning powered football analytics web application** that predicts the **Top players expected to perform best in a match** based on historical Premier League data.

The application allows users to select a **team** and an **opponent team**, then displays the **top ranked players** predicted by the model along with **interactive visualizations**.

---

# 🚀 Project Overview

This project combines **Deep Learning, Data Science, and Web Development** to analyze football player performance.

The system:

1. Uses **5 years of Premier League player data**
2. Trains a **Deep Neural Network model**
3. Predicts **player performance ratings**
4. Ranks players by predicted performance
5. Displays results in a **Flask web application**

---

# 🧠 Deep Learning Model

The model predicts a **player match rating** using match statistics.

### Input Features

* Player name
* Team
* Opponent team
* Minutes played
* Goals
* Assists
* Shots
* Passes completed
* Tackles

### Model Architecture

```
Input Layer
   ↓
Dense Layer (128 neurons, ReLU)
   ↓
Dense Layer (64 neurons, ReLU)
   ↓
Dense Layer (32 neurons, ReLU)
   ↓
Output Layer (Predicted Rating)
```

### Training Details

* Optimizer: **Adam**
* Loss Function: **Mean Squared Error**
* Framework: TensorFlow / Keras
* Validation Split: 20%

---

# 📊 Web Application Features

### 🔎 Team vs Team Prediction

Users select:

* Team
* Opponent Team

The system predicts the **Top 30 players likely to perform best** in the match.

---

### 📋 Player Ranking Table

The results page displays the **Top 30 players sorted by predicted rating**.

| Rank | Player Name | Team   |
| ---- | ----------- | ------ |
| 1    | Player A    | Team A |
| 2    | Player B    | Team B |
| 3    | Player C    | Team B |

---

### 📈 Interactive Visualizations

The results page includes graphs showing:

* Goals distribution
* Assists comparison
* Minutes played analysis

Charts are built using **Chart.js**.

---

# 📂 Project Structure

```
Player-Performance-Prediction
│
├── app.py
├── player_data.pkl
├── premier_league_players_5years_with_rating.csv
├── Player_Performance_Prediction.ipynb
│
├── templates
│   ├── index.html
│   └── result.html
│
├── static
│   └── style.css
│
└── README.md
```

---

# ⚙️ Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/Osamac0d3/Player-Performance-Prediction.git
cd Player-Performance-Prediction
```

### 2️⃣ Install Dependencies

```
pip install flask pandas numpy scikit-learn tensorflow
```

### 3️⃣ Run the Application

```
python app.py
```

Open the browser and go to:

```
http://127.0.0.1:5000
```

---

# 📊 Dataset

Dataset used in this project:

**Premier League Player Performance Dataset (5 Years)**

The dataset contains player match statistics such as:

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

# 🛠️ Technologies Used

* Python
* TensorFlow
* Keras
* Pandas
* NumPy
* Flask
* HTML
* CSS
* Chart.js

---

# 🎯 Future Improvements

* Player **Radar Charts**
* **Top 11 lineup prediction**
* **Team win probability prediction**
* **Advanced deep learning models**
* Full **Football Analytics Dashboard**

---

# 👨‍💻 Author

**Mohd Osama**

GitHub: https://github.com/Osamac0d3

---

# ⭐ Support

If you like this project, consider **starring the repository** ⭐ and contributing to improve the model.
