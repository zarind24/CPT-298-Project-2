import psycopg2
from config.db_config import DB_CONFIG

def load_data(df):
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    insert_query = """
        INSERT INTO maine_towns (town, county, state)
        VALUES (%s, %s, %s)
    """

    for _, row in df.iterrows():
        cursor.execute(insert_query, (row["town"], row["county"], row["state"]))

    conn.commit()
    cursor.close()
    conn.close()