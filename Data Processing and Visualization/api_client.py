import requests


def fetch_student_scores(api_url: str) -> list:
    """
    Fetch data from a public API and map it to student-score format.
    Here, product ratings are treated as test scores.
    """
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        raise RuntimeError(f"Failed to fetch data: {err}")

    data = response.json()
    records = []

    for item in data.get("products", []):
        name = item.get("title")
        score = item.get("rating")

        if name is None or score is None:
            continue

        records.append({
            "name": name,
            "score": float(score)
        })

    return records
