# save_quote.py
import json
from datetime import datetime

def save_quote(quote_details):
    """
    Save the quote details to a JSON file.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"quote_{timestamp}.json"
    with open(filename, "w") as file:
        json.dump(quote_details, file, indent=4)
    print(f"Quote saved to {filename}")

def share_quote(quote_details):
    """
    Simulate sharing the quote (e.g., via email or messaging).
    """
    print("Sharing quote...")
    print(json.dumps(quote_details, indent=4))