def calculate_total(price, quantity):
    """Calculate the total cost of an order."""
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity cannot be negative")

    return price * quantity


if __name__ == "__main__":
    total = calculate_total(25.00, 3)
    print(f"Order total: £{total:.2f}")
