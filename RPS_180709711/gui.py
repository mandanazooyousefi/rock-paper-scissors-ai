import tkinter as tk
import csv
from ai_model import prepare_dataset, train_model, predict_next_move
from random import choice

# Global skorlar
player_score = 0
ai_score = 0

# AI hamlesi tahmini
def get_ai_move():
    X, y, le = prepare_dataset()
    if X is None:
        return choice(["rock", "paper", "scissors"])
    model = train_model(X, y)
    recent = X[-1]
    recent_labels = le.inverse_transform(recent)
    predicted = predict_next_move(model, recent_labels, le)
    counter = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    return counter[predicted]

# Kazananı belirle ve skor güncelle
def determine_winner(player, ai):
    global player_score, ai_score
    if player == ai:
        return "Berabere!"
    elif (player == "rock" and ai == "scissors") or \
         (player == "scissors" and ai == "paper") or \
         (player == "paper" and ai == "rock"):
        player_score += 1
        return "Sen kazandın!"
    else:
        ai_score += 1
        return "AI kazandı!"

# Oyun oynanır
def play(move):
    ai_move = get_ai_move()
    result = determine_winner(move, ai_move)
    result_label.config(text=f"Sen: {move} | AI: {ai_move} → {result}")
    score_label.config(text=f"Skor: Sen {player_score} - {ai_score} AI")
    save_choice(move)

# Hamleyi kaydet
def save_choice(choice):
    with open("data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([choice])

# Skorları ve sonucu sıfırla
def reset_game():
    global player_score, ai_score
    player_score = 0
    ai_score = 0
    result_label.config(text="")
    score_label.config(text="Skor: Sen 0 - 0 AI")

# Arayüz
root = tk.Tk()
root.title("Rock Paper Scissors - AI")
root.geometry("400x300")

title = tk.Label(root, text="AI ile Rock Paper Scissors", font=("Helvetica", 16, "bold"))
title.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="🪨 Rock", width=10, command=lambda: play("rock"))
paper_btn = tk.Button(button_frame, text="📄 Paper", width=10, command=lambda: play("paper"))
scissors_btn = tk.Button(button_frame, text="✂️ Scissors", width=10, command=lambda: play("scissors"))

rock_btn.grid(row=0, column=0, padx=10)
paper_btn.grid(row=0, column=1, padx=10)
scissors_btn.grid(row=0, column=2, padx=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Skor: Sen 0 - 0 AI", font=("Helvetica", 12, "bold"))
score_label.pack(pady=5)

reset_btn = tk.Button(root, text="🔄 Reset", command=reset_game)
reset_btn.pack(pady=10)

root.mainloop()
