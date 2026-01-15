def calculate_average(records: list) -> float:
    if not records:
        return 0.0

    total = sum(item["score"] for item in records)
    return round(total / len(records), 2)
    """Calculating the average score from a list of student-score records."""