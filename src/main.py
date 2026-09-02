from src.pipeline.step_one import ingest_data
from src.pipeline.step_two import transform_data
from src.pipeline.step_three import load_data


def run_pipeline():
    df = ingest_data()
    df = transform_data(df)
    load_data(df)

if __name__ == "__main__":
    run_pipeline()
