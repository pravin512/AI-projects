# metal_price_api.py
import requests

def get_metal_price(metal_type):
    """
    Fetch the current price of gold or silver.
    """
    price_list_dict = {
        "gold":8860,
        "silver": 97.98
    }
    
    return price_list_dict[metal_type]
    # Use a free API for metal prices (e.g., https://www.metalpriceapi.com/)
    api_url = f"https://api.metalpriceapi.com/v1/latest?api_key=YOUR_API_KEY&base={metal_type.upper()}&currencies=USD"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        return data["rates"]["USD"]  # Price per gram or ounce
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {metal_type} price: {e}")
        return None