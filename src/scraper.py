import sqlite3
import pandas as pd
from datetime import datetime

DB_PATH = "data/prices.db"


def init_db():
    """Creates the database table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS phone_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            model TEXT,
            condition TEXT,
            price REAL,
            source TEXT
        )
    """)
    conn.commit()
    conn.close()
    print("Database initialized.")


def fetch_current_prices():
    """
    Week 1 Mock Data: Simulating data extraction.
    Later, we'll replace this with real web scraping or API calls.
    """
    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Fetching data for {today}...")

    data = [
        {"timestamp": today, "model": "Google Pixel 8 128GB", "condition": "New", "price": 499.00,
         "source": "Target Store A"},
        {"timestamp": today, "model": "Samsung Galaxy S24 128GB", "condition": "New", "price": 699.00,
         "source": "Target Store B"},
        {"timestamp": today, "model": "iPhone 15 Pro 256GB", "condition": "Refurbished", "price": 850.00,
         "source": "Target Store A"}
    ]
    return pd.DataFrame(data)


def save_to_db(df):
    """Appends the dataframe records directly into the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    df.to_sql("phone_prices", conn, if_exists="append", index=False)
    conn.close()
    print(f"Successfully inserted {len(df)} records into {DB_PATH}.")


if __name__ == "__main__":
    init_db()
    latest_data = fetch_current_prices()
    save_to_db(latest_data)