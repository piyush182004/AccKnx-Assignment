import csv
import sqlite3

def store_csv_in_db():
    # connect to database (creates it if not present)
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    # create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    """)

    # read CSV file
    with open("users.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute(
                "INSERT INTO users (name, email) VALUES (?, ?)",
                (row["name"], row["email"])
            )

    connection.commit()
    connection.close()
    print("Data stored in database successfully")


store_csv_in_db()
