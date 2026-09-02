import json
import pandas as pd
from src.utils.logger import get_logger

logger = get_logger(__name__)

def ingest_data():
    logger.info("Starting ingestion step...")

    try:
        with open("data/transactions.json", "r") as f:
            data = json.load(f)

        df = pd.DataFrame(data)
        logger.info(f"Ingestion complete. Loaded {len(df)} rows.")
        return df

    except Exception as e:
        logger.error(f"Ingestion failed: {e}")
        raise
