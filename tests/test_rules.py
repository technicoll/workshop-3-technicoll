from rules import will_buy_drink

def test_loyalty_lunch_true():
    assert will_buy_drink({"time_of_day": "lunch", "loyalty_member": "yes"}) is True

def test_non_loyalty_lunch_false():
    assert will_buy_drink({"time_of_day": "lunch", "loyalty_member": "no"}) is False

def test_loyalty_evening_false():
    assert will_buy_drink({"time_of_day": "evening", "loyalty_member": "yes"}) is False

def test_heatwave_evening_non_loyalty_true():
    assert will_buy_drink({"time_of_day": "evening", "loyalty_member": "no", "temperature": 32}) is True

def test_large_order_true():
    assert will_buy_drink({"time_of_day": "evening", "loyalty_member": "no", "temperature": 20, "order_size": 4}) is True

def test_busy_heatwave_lunch_non_loyalty_false():
    assert will_buy_drink({"time_of_day": "lunch", "loyalty_member": "no", "temperature": 32}) is False
