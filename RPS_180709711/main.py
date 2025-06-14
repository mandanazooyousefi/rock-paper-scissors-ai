import csv
from ai_model import prepare_dataset, train_model, predict_next_move

def get_user_choice():
    choice = input("Hamleni seç (rock/paper/scissors veya q ile çık): ").lower()
    while choice not in ["rock", "paper", "scissors", "q"]:
        choice = input("Geçersiz! Lütfen rock/paper/scissors yaz (q ile çık): ").lower()
    return choice

def save_choice(choice):
    with open("data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([choice])

def determine_winner(player, ai):
    if player == ai:
        return "Berabere!"
    elif (player == "rock" and ai == "scissors") or \
         (player == "scissors" and ai == "paper") or \
         (player == "paper" and ai == "rock"):
        return "Sen kazandın!"
    else:
        return "AI kazandı!"

def get_ai_move():
    X, y, le = prepare_dataset()
    if X is None:
        return None  # Yeterli veri yoksa rastgele oynasın
    model = train_model(X, y)
    recent = X[-1]  # En son 3 hamleyi al
    recent_labels = le.inverse_transform(recent)
    predicted = predict_next_move(model, recent_labels, le)
    
    # Kazanacak hamleyi seç
    counter = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    return counter[predicted]

def main():
    print("🎮 Rock-Paper-Scissors AI ile Oyna\n")

    while True:
        user_move = get_user_choice()
        if user_move == "q":
            print("Görüşmek üzere 👋")
            break

        ai_move = get_ai_move()
        if ai_move is None:
            from random import choice
            ai_move = choice(["rock", "paper", "scissors"])

        print(f"AI hamlesi: {ai_move}")
        result = determine_winner(user_move, ai_move)
        print(result + "\n")

        save_choice(user_move)

if __name__ == "__main__":
    main()
