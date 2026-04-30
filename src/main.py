from src.extract import fetch_data
from src.transform import transform_data
from src.load import load_data

def main():
    print("Fetching data...")
    raw_data = fetch_data()

    print("Transforming data...")
    df = transform_data(raw_data)

    print("Loading data into PostgreSQL...")
    load_data(df)

    print("Done!")

if __name__ == "__main__":
    main()