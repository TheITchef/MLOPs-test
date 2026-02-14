import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame."""
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the DataFrame by dropping missing values."""
    return df.dropna()


def compute_mean(df: pd.DataFrame, column: str) -> float:
    """Compute the mean of a specific column."""
    return df[column].mean()


def run_pipeline():
    # Load the new dataset
    df = load_data("data/example2.csv")

    # Clean the data
    df = clean_data(df)

    # Compute the mean
    mean_value = compute_mean(df, "value")

    print(f"Mean value: {mean_value}")


if __name__ == "__main__":
    run_pipeline()
