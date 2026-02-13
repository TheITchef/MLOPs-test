import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Load a CSV file into a DataFrame."""
    return pd.read_csv(path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Simple cleaning: drop rows with missing values."""
    return df.dropna()

def compute_mean(df: pd.DataFrame, column: str) -> float:
    """Compute the mean of a numeric column."""
    return df[column].mean()

def run_pipeline():
    df = load_data("data/sample.csv")
    df = clean_data(df)
    mean_value = compute_mean(df, "value")
    print(f"Mean value: {mean_value}")

if __name__ == "__main__":
    run_pipeline()

