## Step 2 – TDD Cycle 1 (Red → Green)

**Cell 3 – Create function and tests**

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

**Reflect:** What’s the smallest logic that barely passes both tests?