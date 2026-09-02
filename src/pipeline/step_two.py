import pandas as pd
from src.utils.logger import get_logger

logger = get_logger(__name__)

def transform_data(df):
    logger.info("Starting transformation step...")

    # Drop duplicates
    df = df.drop_duplicates()

    # Convert timestamps
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    # Add derived field
    df["is_failed"] = df["status"] == "failed"

    # Handle missing values
    df["error_code"] = df["error_code"].fillna("NONE")

    logger.info("Transformation complete.")
    return df
