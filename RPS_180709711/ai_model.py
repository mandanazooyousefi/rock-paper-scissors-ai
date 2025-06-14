
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Eğitim verisini hazırla
def prepare_dataset(file_path="data.csv", history_size=3):
    df = pd.read_csv(file_path, header=None, names=["move"])
    
    if len(df) <= history_size:
        return None, None, None
    
    X = []
    y = []
    
    for i in range(history_size, len(df)):
        prev_moves = df["move"].iloc[i-history_size:i].tolist()
        next_move = df["move"].iloc[i]
        X.append(prev_moves)
        y.append(next_move)
    
   
    le = LabelEncoder()
    all_moves = ["rock", "paper", "scissors"]
    le.fit(all_moves)
    
    X_encoded = [le.transform(x).tolist() for x in X]
    y_encoded = le.transform(y)
    
    return X_encoded, y_encoded, le


def train_model(X, y):
    clf = DecisionTreeClassifier()
    clf.fit(X, y)
    return clf


def predict_next_move(model, recent_moves, le):
    encoded = le.transform(recent_moves).reshape(1, -1)
    pred = model.predict(encoded)[0]
    return le.inverse_transform([pred])[0]


if __name__ == "__main__":
    X, y, le = prepare_dataset()
    if X is None:
        print("Yeterli veri yok. Lütfen önce biraz veri toplayın.")
    else:
        model = train_model(X, y)
        tahmin = predict_next_move(model, ["rock", "paper", "scissors"], le)
        print(f"Tahmin edilen bir sonraki hamle: {tahmin}")
