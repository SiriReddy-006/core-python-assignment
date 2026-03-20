ratings = [5, 4, 3, 5, 2, 4, 1, 5]

def pos_percent():
    positive_count = 0
    total_count = len(ratings)
    for r in ratings:
        if r >= 4:
            positive_count = positive_count + 1

    if total_count == 0:
        print("No ratings available")
        return
    percent = (positive_count / total_count) * 100
    print("Positive Feedback:", percent, "%")

pos_percent()
