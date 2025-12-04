```python
def will_buy_drink(order: dict) -> bool:
    """Predict if a customer will buy a drink."""
    if order["loyalty_member"] == "no":
        return False

    return True
```