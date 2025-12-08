from rules import will_buy_drink
from logging_utils import log_experiment

def main():
    order_to_log = {"time_of_day": "lunch", "loyalty_member": "yes"}
    prediction = will_buy_drink(order_to_log)
    print("Prediction:", prediction)
    log_experiment(order_to_log, prediction, run_name="Initial Loyalty Rule")

if __name__ == "__main__":
    main()
