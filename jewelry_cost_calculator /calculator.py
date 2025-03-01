# calculator.py

def calculate_metal_cost(weight, purity, metal_price_per_gram, metal_type):
    """
    Calculate the cost of gold or silver based on weight, purity, and current price.
    """
    if metal_type.lower() == "gold":
        purity_percentage = purity / 24  # Convert karat to percentage
    elif metal_type.lower() == "silver":
        purity_percentage = purity / 100  # Silver purity is in percentage (e.g., 92.5% for sterling silver)
    else:
        raise ValueError("Invalid metal type. Choose 'gold' or 'silver'.")
    
    metal_cost = weight * metal_price_per_gram * purity_percentage
    return metal_cost