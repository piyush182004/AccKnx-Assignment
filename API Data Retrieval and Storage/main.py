from api_client import fetch_books
from database import (
    create_books_table,
    insert_books,
    fetch_books_from_db
)

API_URL = (
    "https://openlibrary.org/search.json"
    "?q=harry+potter"
    "&fields=title,author_name,first_publish_year"
    "&limit=10"
)


def main():
    create_books_table()

    books = fetch_books(API_URL)
    insert_books(books)

    stored_books = fetch_books_from_db()
    print("Books stored in database:\n")

    for title, author, year in stored_books:
        print(f"{title} | {author} | {year}")


if __name__ == "__main__":
    main()
