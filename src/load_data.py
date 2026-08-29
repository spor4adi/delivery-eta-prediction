from config import DATA_PATH
import pandas as pd


def load_data(path=DATA_PATH):
    """
    Load a CSV file into a pandas DataFrame.
    """
    try:
        df = pd.read_csv(path)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Could not find data file at: {path}") from e
    if df.empty:
        raise ValueError(f"Expected a non-empty dataset, but got 0 rows from: {path}")

    return df


if __name__ == "__main__":
    df = load_data(DATA_PATH)
    print(df.head())