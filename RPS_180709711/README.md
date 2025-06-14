

## Student Info

- **Name:** Mandana Zooyousefin  
- **Student ID:** 180709711  
- **Advisor:** Dr. Bekir Taner Dinçer  
- **Course:** CENG 3511 – Artificial Intelligence  

---

# Rock-Paper-Scissors AI Agent

A simple machine learning-powered **AI agent** that plays **Rock-Paper-Scissors** by analyzing the player’s previous moves and predicting the next move using a **Decision Tree Classifier**.

---

## Project Overview

**Class**: CENG 3511 – Artificial Intelligence  
**Project Name**: Rock-Paper-Scissors AI Agent  
**Goal**: To design and implement an AI that can act as an opponent in a Rock-Paper-Scissors game using a classification model trained on previous human inputs.

---

## ✨ Features

- GUI interface built with **Tkinter**
- Learns from player’s past 3 moves using supervised ML
- Predicts player’s next move
- Plays the optimal counter move
- Score tracking and reset functionality
- Game data stored and updated in `data.csv`

---

## 📂 Folder Structure

rock-paper-scissors-ai/
├── main.py # Terminal-based gameplay and data logging
├── gui.py # Tkinter GUI gameplay with AI agent
├── ai_model.py # ML model training and prediction logic
├── data.csv # Player move history for training
├── README.md # Project description and usage guide



---

## 🛠️ Technologies Used

- Python 3.11+
- scikit-learn (DecisionTreeClassifier)
- pandas, numpy
- tkinter (built-in GUI library)

---

## ▶️ How to Run

1.git clone [https://github.com/your-username/rock-paper-scissors-ai.git
   cd rock-paper-scissors-ai](https://github.com/mandanazooyousefi/rock-paper-scissors-ai)
2.Install Required Packages
    pip install scikit-learn pandas numpy
3.Launch the graphical interface:
    python gui.py
4.Play with the AI
   Choose Rock , Paper , or Scissors 
    The AI will predict your next move and play the counter
    The game keeps score and learns from your past moves via data.csv 
