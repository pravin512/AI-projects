# gemstone_calculator.py

def calculate_gemstone_cost(gemstone_type, carat_weight, quality_factor):
    """
    Calculate the cost of gemstones based on type, carat weight, and quality.
    """
    # Example prices (replace with actual market prices)
    gemstone_prices = {
        "diamond": 5000,  # Price per carat
        "sapphire": 1000,
        "ruby": 1200,
        "emerald": 800,
    }
    
    if gemstone_type.lower() not in gemstone_prices:
        raise ValueError("Invalid gemstone type.")
    
    base_price = gemstone_prices[gemstone_type.lower()]
    total_gemstone_cost = base_price * carat_weight * quality_factor
    return total_gemstone_cost