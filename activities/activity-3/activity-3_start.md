## Step 3 – TDD Cycle 2 (+ Intro to MLflow)

**Cell 4 – Add a new test**

    # Evening loyalty → should NOT be upsold
    order_2 = {"time_of_day": "evening", "loyalty_member": "yes"}
    assert will_buy_drink(order_2) is False, "FAIL: Evening loyalty should NOT be upsold."
    print("PASS: Test 2")

Now your logic must consider both `time_of_day` and `loyalty_member` to make all tests green.

**Cell 5 – Log experiment with MLflow**

    try:
        import mlflow
        mlflow.set_tracking_uri("file:./mlruns")
        mlflow.set_experiment("hotdog-upsell")
        with mlflow.start_run(run_name="Initial Loyalty Rule"):
            order = {"time_of_day": "lunch", "loyalty_member": "yes"}
            prediction = will_buy_drink(order)
            mlflow.log_params(order)
            mlflow.log_metric("prediction", int(bool(prediction)))
            mlflow.set_tag("rule_version", "v1")
        print("Experiment logged successfully ✅")
    except Exception:
        print("[INFO] MLflow not installed — skipping logging safely.")