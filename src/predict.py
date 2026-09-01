from pathlib import Path
import joblib
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "student_model.pkl"


def predict(
    study_hours,
    attendance,
    previous_score,
    sleep_hours
):

    model = joblib.load(MODEL_PATH)

    data = pd.DataFrame([
        {
            "study_hours": study_hours,
            "attendance": attendance,
            "previous_score": previous_score,
            "sleep_hours": sleep_hours
        }
    ])

    prediction = model.predict(data)[0]

    prediction = max(
        0,
        min(100, prediction)
    )

    return prediction


if __name__ == "__main__":

    result = predict(
        study_hours=6,
        attendance=92,
        previous_score=75,
        sleep_hours=7
    )

    print(
        f"Predicted Score: {result:.2f}"
    )
