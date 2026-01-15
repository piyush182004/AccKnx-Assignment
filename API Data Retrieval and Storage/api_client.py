import requests


def fetch_books(api_url: str) -> list:
    """
    Fetches book data from an external REST API.
    Returns a list of dictionaries with title, author, and year.
    """
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        raise RuntimeError(f"API request failed: {error}")

    payload = response.json()
    books = []

    for record in payload.get("docs", []):
        title = record.get("title")
        authors = record.get("author_name")
        year = record.get("first_publish_year")

        if not title or not authors:
            continue

        books.append({
            "title": title.strip(),
            "author": authors[0].strip(),
            "year": year
        })

    return books
