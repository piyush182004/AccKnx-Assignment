import sqlite3

DB_NAME = "books.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_books_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publication_year INTEGER,
            UNIQUE(title, author)
        )
    """)

    conn.commit()
    conn.close()


def insert_books(books: list):
    conn = get_connection()
    cursor = conn.cursor()

    for book in books:
        cursor.execute(
            """
            INSERT OR IGNORE INTO books (title, author, publication_year)
            VALUES (?, ?, ?)
            """,
            (book["title"], book["author"], book["year"])
        )

    conn.commit()
    conn.close()


def fetch_books_from_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT title, author, publication_year
        FROM books
        ORDER BY publication_year DESC
    """)

    results = cursor.fetchall()
    conn.close()
    return results
