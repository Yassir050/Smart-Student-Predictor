import pandas as pd


FEATURES = [
    "study_hours",
    "attendance",
    "previous_score",
    "sleep_hours"
]

TARGET = "final_score"


def load_data(path):
    return pd.read_csv(path)


def prepare_data(path):
    df = load_data(path)

    df = df.dropna()

    X = df[FEATURES]
    y = df[TARGET]

    return X, y
