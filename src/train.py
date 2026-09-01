from pathlib import Path
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

from preprocess import prepare_data


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "students.csv"
MODEL_PATH = BASE_DIR / "models" / "student_model.pkl"


def train():

    X, y = prepare_data(DATA_PATH)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = LinearRegression()

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    r2 = r2_score(
        y_test,
        predictions
    )

    MODEL_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    joblib.dump(
        model,
        MODEL_PATH
    )

    print("Training completed.")
    print(f"MAE: {mae:.2f}")
    print(f"R²: {r2:.2f}")
    print(f"Model saved to: {MODEL_PATH}")


if __name__ == "__main__":
    train()
