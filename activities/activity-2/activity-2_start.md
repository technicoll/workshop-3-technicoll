## Expected outputs
You will add Python code to an incomplete function so that two unit tests pass.

## Step 2 – TDD Cycle 1 (Red → Green)
Continue working in the same notebook from your previous cycle.

**Cell 3 – Create function and tests**

Create a new Code cell containing the following:

```python
def will_buy_drink(order: dict) -> bool:
    """Predict if a customer will buy a drink."""
    return None  # start with a failing stub (RED)


# Positive test – loyalty at lunch → True
order_1a = {"time_of_day": "lunch", "loyalty_member": "yes"}
assert will_buy_drink(order_1a) is True, "FAIL: Loyalty at lunch should be upsold."
print("PASS: Test 1a")

# Negative test – non-loyalty at lunch → False (prevents `return True`)
order_1b = {"time_of_day": "lunch", "loyalty_member": "no"}
assert will_buy_drink(order_1b) is False, "FAIL: Non-loyalty at lunch should NOT be upsold."
print("PASS: Test 1b")
```

This code codes a function `will_buy_drink()` and two unit tests. The unit tests are correct but the function is incomplete.

Run the code and note that you receive an `AssertionError`. This means that one or more of your unit tests aren't passing. This is due to the incomplete function.

Your task is to modify the code in the `will_buy_drink()` function so that the tests pass. You can re-run the same Code cell regularly to test your code.

You'll know you've succeeded when the output is:

```
PASS: Test 1a
PASS: Test 1b
```

## Hints
- **Reflect:** What’s the smallest logic that barely passes both tests?
- Try to fix one test at a time and build up the logic.
- What are the essential features of your function? What is the argument? What is the argument's type? What is the type of the return value?