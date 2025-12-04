```python
def will_buy_drink(order: dict) -> bool:
    """Predict if a customer will buy a drink."""
    if order["loyalty_member"] == "no":
        return False

    return True


# Positive test – loyalty at lunch → True
order_1a = {"time_of_day": "lunch", "loyalty_member": "yes"}
assert will_buy_drink(order_1a) is True, "FAIL: Loyalty at lunch should be upsold."
print("PASS: Test 1a")

# Negative test – non-loyalty at lunch → False (prevents `return True`)
order_1b = {"time_of_day": "lunch", "loyalty_member": "no"}
assert will_buy_drink(order_1b) is False, "FAIL: Non-loyalty at lunch should NOT be upsold."
print("PASS: Test 1b")
```