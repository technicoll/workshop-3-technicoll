# Corndel – Level 6 Applied AI Engineering
## Workshop 3 – Upsell Like an Engineer

Hands-on workshop moving from exploratory notebooks to disciplined, professional Python for machine learning.

> 💡 We’re not teaching AWS — we’re teaching transferable engineering habits.

---

## Learning Intent

By the end of this workshop you will:

- Write code that is **testable**, **maintainable**, and **reproducible**  
- Practise **TDD** (Red → Green → Refactor) on a simple upsell predictor  
- **Log experiments** locally with MLflow  
- **Refactor** safely using tests as a safety net  
- Connect these habits to **risk reduction** and **technical debt**

---

# Master Notebook Guide (Single Notebook Flow)

We’ll work in **one Jupyter notebook** for the whole day.  
Follow each section below and add one code cell at a time.

> **Tip:** Use Markdown headings inside your notebook to mirror these steps.

---

## Step 0 – Create Your Notebook

1. In JupyterLab, click **File → New → Notebook**.  
2. Choose the **conda_python3** kernel (or your default Python 3).  
3. Rename it to **Workshop3W_Master.ipynb**.

**Add this as your first Markdown cell:**

    # Workshop 3W — Upsell Like an Engineer
    Unit 3 — Programming for Intelligent Products

    Today we’ll practise TDD (Red → Green → Refactor), experiment logging, and debugging discipline.

---

## Step 1 – Set Up Your Environment (then restart kernel)

**Cell 1 – Install packages**

    !pip uninstall -y mlflow mlflow-skinny mlflow-tracing || true
    !pip install "mlflow==2.15.1" pandas scikit-learn
    print("Installed requirements. Please restart the kernel now.")

> After this runs, go to **Kernel → Restart Kernel**.

**Cell 2 – Verify**

    import sys, platform
    print("Python:", sys.version)
    print("Platform:", platform.platform())
    import mlflow, pandas as pd
    print("MLflow:", mlflow.__version__)
    print("Environment ready ✅")

---

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

---

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

---

## Step 4 – Refactoring Cycle

**Cell 6 – Extend tests**

    # Heatwave → True
    order_3 = {"time_of_day": "evening", "loyalty_member": "no", "temperature": 32}
    assert will_buy_drink(order_3) is True, "FAIL: Hot weather should trigger upsell."
    print("PASS: Test 3")

    # Large order → True
    order_4 = {"order_size": 4}
    assert will_buy_drink(order_4) is True, "FAIL: Large orders should trigger upsell."
    print("PASS: Test 4")

**Cell 7 – Refactor safely**

    def will_buy_drink(order: dict) -> bool:
        """Simple rule-based upsell logic."""
        if order.get("temperature", 0) > 30: return True
        if order.get("order_size", 0) >= 4: return True
        if order.get("loyalty_member") == "yes" and order.get("time_of_day") == "lunch": return True
        return False

Run all previous tests — they should still pass ✅

---

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

---

## Step 6 – Git Simulation & Reflection

**Cell 10 – Simulated commit log**

    print("### My Commit Log")
    commits = [
        "feat: Add initial failing test for lunch loyalty",
        "fix: Implement lunch loyalty rule",
        "feat: Add evening loyalty test",
        "fix: Handle time-of-day logic",
        "refactor: Simplify function and add docstring",
        "fix: Add busy heatwave override"
    ]
    for c in commits: print("-", c)

**Markdown reflection cell:**

    ### Reflection
    - What technical debt did you remove today?  
    - How did tests act as your safety net?  
    - Which step felt most like professional engineering?

---

## Running Tests Locally

After completing the notebook, the final function lives in `src/hotdog/rules.py`.  
You can test it outside Jupyter like a real module.

Run from the terminal:

    PYTHONPATH=src pytest -q

or on Windows:

    set PYTHONPATH=src; pytest -q

This executes `tests/test_rules.py` and prints concise results (e.g. `6 passed in 0.04s`).

---

## MLflow Logging

MLflow acts as your digital lab notebook.

All runs are stored locally under:

    file:./mlruns

### What Happens
1. Experiment “hotdog-upsell” is created or reused.  
2. Run “Initial Loyalty Rule” starts.  
3. Inputs and outputs are logged as parameters and metrics.  
4. A tag `rule_version=v1` is added for traceability.  

### Safe Logging
If MLflow isn’t installed, `src/hotdog/logging_utils.py` prints:

    [INFO] MLflow not installed — skipping logging.

Enable it anytime with:

    pip install mlflow==2.15.1

### Optional Script
Run the same logic outside Jupyter:

    PYTHONPATH=src python scripts/run_mlflow_example.py

---

## Going Further (Optional)

Export your notebook as a script for production pipelines.  
See [Convert notebook code into Python scripts – Azure Machine Learning (Microsoft Learn)](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-convert-ml-experiment-to-production?view=azureml-api-1)
