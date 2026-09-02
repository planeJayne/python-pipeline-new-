import json
import random
import uuid
from datetime import datetime, timedelta

def generate_transactions(num_rows=5000):
    merchants = ["Amazon", "Walmart", "Target", "Uber", "Delta", "Apple", "Starbucks", "Costco"]
    categories = ["Shopping", "Travel", "Groceries", "Electronics", "Dining", "Utilities"]
    currencies = ["USD", "EUR", "JPY", "GBP"]
    countries = ["US", "UK", "JP", "DE", "FR", "CA"]
    device_types = ["mobile", "web", "tablet"]
    statuses = ["success", "failed", "pending"]
    error_codes = [None, "E001", "E002", "E003"]

    data = []

    for _ in range(num_rows):
        status = random.choice(statuses)
        error = random.choice(error_codes) if status == "failed" else None

        row = {
            "transaction_id": str(uuid.uuid4()),
            "customer_id": f"C{random.randint(1000, 9999)}",
            "amount": round(random.uniform(5.0, 500.0), 2),
            "currency": random.choice(currencies),
            "merchant": random.choice(merchants),
            "category": random.choice(categories),
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 365))).isoformat(),
            "status": status,
            "error_code": error,
            "country": random.choice(countries),
            "device_type": random.choice(device_types)
        }

        data.append(row)

    with open("data/transactions.json", "w") as f:
        json.dump(data, f, indent=2)

    print("Generated data/transactions.json with", num_rows, "rows")

if __name__ == "__main__":
    generate_transactions()
