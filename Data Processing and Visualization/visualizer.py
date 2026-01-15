import matplotlib.pyplot as plt


def plot_scores(records: list, average: float):
    names = [item["name"] for item in records[:10]]
    scores = [item["score"] for item in records[:10]]

    plt.figure()
    plt.bar(names, scores)
    plt.axhline(average, linestyle="--", label=f"Average: {average}")
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Students")
    plt.ylabel("Score")
    plt.title("Student Test Scores (Derived from Public API)")
    plt.legend()
    plt.tight_layout()

    plt.savefig("student_scores.png", dpi=300)
    plt.show()
