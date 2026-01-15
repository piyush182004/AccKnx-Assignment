from api_client import fetch_student_scores
from processor import calculate_average
from visualizer import plot_scores

API_URL = "https://dummyjson.com/products"


def main():
    records = fetch_student_scores(API_URL)

    average_score = calculate_average(records)
    print(f"Average Score: {average_score}")

    plot_scores(records, average_score)


if __name__ == "__main__":
    main()
