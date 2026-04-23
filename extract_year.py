from datetime import datetime

dt = datetime(2026, 5, 12)

# Lambda function
extract_date = lambda d: (d.year, d.month, d.day)

result = extract_date(dt)

print(result)