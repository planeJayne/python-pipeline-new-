from src.utils.logger import get_logger

logger = get_logger(__name__)

def load_data(df):
    logger.info("Starting load step...")

    output_path = "data/processed_transactions.csv"
    df.to_csv(output_path, index=False)

    logger.info(f"Load complete. Saved processed data to {output_path}.")
