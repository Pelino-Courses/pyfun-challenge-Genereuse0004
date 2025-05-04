from datetime import datetime
def date_difference(start_date: str, end_date: str):
    try:
        date_format = "%Y-%m-%d"
        d1 = datetime.strptime(start_date, date_format)
        d2 = datetime.strptime(end_date, date_format)
        return abs((d2 - d1).days)
    except ValueError:
        return "Error: Please provide dates in YYYY-MM-DD format."
if __name__ == "__main__":
    print(date_difference("2025-05-01", "2025-05-04"))
    print(date_difference("2025-05-01", "wrong-date"))
        