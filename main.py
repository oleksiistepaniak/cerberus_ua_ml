import pandas as pd
from models.baseline import get_baseline_model
from utils.preprocessing import clean_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

df = pd.read_csv("data/example.csv")
df["text"] = df["text"].apply(clean_text)

X_train, X_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.3, random_state=42)

model = get_baseline_model()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))
