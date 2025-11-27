## Step 5 – Debugging Challenge

**Cell 8 – Failing test for a new rule**

    # Busy lunch heatwave (non-loyalty) → should NOT upsell
    order_5 = {"time_of_day": "lunch", "loyalty_member": "no", "temperature": 32}
    assert will_buy_drink(order_5) is False, "FAIL: Busy lunch heatwave (non-loyalty) should NOT upsell."
    print("PASS: Test 5")

**Cell 9 – Add override logic**

    def will_buy_drink(order: dict) -> bool:
        time = str(order.get("time_of_day", "")).strip().lower()
        loyalty = str(order.get("loyalty_member", "no")).strip().lower()
        temp = int(order.get("temperature", 0) or 0)
        size = int(order.get("order_size", 0) or 0)
        if temp > 30 and time == "lunch" and loyalty != "yes": return False
        if temp > 30: return True
        if size >= 4: return True
        if loyalty == "yes" and time == "lunch": return True
        return False

Check that all previous tests still pass.