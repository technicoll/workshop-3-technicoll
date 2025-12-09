## Step 4 – Refactoring Cycle

**Cell 6 – Extend tests**

    # Heatwave → True
    order_3 = {"time_of_day": "evening", "loyalty_member": "no", "temperature": 32}
    assert should_upsell(order_3) is True, "FAIL: Hot weather should trigger upsell."
    print("PASS: Test 3")

    # Large order → True
    order_4 = {"order_size": 4}
    assert should_upsell(order_4) is True, "FAIL: Large orders should trigger upsell."
    print("PASS: Test 4")

**Cell 7 – Refactor safely**

    def should_upsell(order: dict) -> bool:
        """Simple rule-based upsell logic."""
        if order.get("temperature", 0) > 30: return True
        if order.get("order_size", 0) >= 4: return True
        if order.get("loyalty_member") == "yes" and order.get("time_of_day") == "lunch": return True
        return False

Run all previous tests — they should still pass ✅