## Expected outputs
You'll create a Jupyter Notebook in your Codespace or local environment (using the venv you set up from the README). You'll verify the environment so you're ready to progress with the rest of the workshop. By the end, you'll have:
- One Markdown cell.
- Two Code cells that you've successfully run.

## Step 0 – Create Your Notebook

1. Make sure you’ve created and activated the venv per the README, and installed dependencies with `pip install -r requirements.txt` (repeat here for completeness).
2. In JupyterLab, click **File → New → Notebook**.  
3. Choose the kernel for your venv (use the **Select Kernel** button if needed).  
4. Rename the new notebook to **Workshop3W_Master.ipynb** by right-clicking it in the explorer on the left and selecting "Rename".
5. Modify the first cell in your notebook so that it's a Markdown cell. You can do this by clicking on the dropdown menu in the notebook tab command bar that says "Code" by default, then selecting "Markdown" from the menu.

**Add this as your first Markdown cell:**

    # Workshop 3W — Upsell Like an Engineer
    Unit 3 — Programming for Intelligent Products

    Today we’ll practise TDD (Red → Green → Refactor), experiment logging, and debugging discipline.

---

## Step 1 – Verify your environment (then restart kernel)

You should already have the venv activated and dependencies installed (per the README). Ensure your notebook is using that venv’s kernel, then verify:

**Cell 1 – Verify**

Create a new Code cell:

```python
import sys, platform
print("Python:", sys.version)
print("Platform:", platform.platform())
import mlflow, pandas as pd
print("MLflow:", mlflow.__version__)
print("Environment ready ✅")
```

Run this and ignore any warnings about deprecated packages. (In production code, you should pay attention to these and take action, but it's not vital today.)

Ensure that the MLflow version is 2.15.1 and you see `Environment ready ✅`.

This diagram shows the full rule-based logic for deciding when to upsell a drink, and in Activities 2, 3, 4, and 5 you’ll build it up step by step: starting with a simple “loyalty at lunch” rule, extending it to other times of day, then adding heatwave and large-order rules, and finally introducing a special override for busy lunch heatwaves.


                           ┌──────────────────────────────┐
                           │ Start: Evaluate order input   │
                           └───────────────┬──────────────┘
                                           │
                                           ▼
        ┌───────────────────────────────────────────────────────────────┐
        │ Rule from Cycle 1: Is loyalty_member "yes" AND time_of_day    │
        │ == "lunch"?                                                    │
        └───────────────────────────────┬───────────────────────────────┘
                                        │ Yes
                                        ▼
                                 ┌────────────┐
                                 │  RETURN    │
                                 │   TRUE     │ (Loyal customer at lunch)
                                 └────────────┘
                                        │
                                        │ No
                                        ▼
        ┌───────────────────────────────────────────────────────────────┐
        │ Rule from Cycle 2: Is time_of_day NOT "lunch"?                │
        │ (e.g., evening loyalty → no upsell)                           │
        └───────────────────────────────┬───────────────────────────────┘
                                        │ Yes
                                        ▼
                                 ┌────────────┐
                                 │  RETURN    │
                                 │   FALSE    │ (Outside lunch → no upsell)
                                 └────────────┘
                                        │
                                        │ No (still lunch)
                                        ▼
                    ┌────────────────────────────────────────────┐
                    │ Refactor rules: Is temperature > 30?       │
                    └───────────────────────┬────────────────────┘
                                            │ Yes
                                            ▼
                                     ┌────────────┐
                                     │  RETURN    │
                                     │   TRUE     │ (Heatwave upsell)
                                     └────────────┘
                                            │
                                            │ No
                                            ▼
                  ┌───────────────────────────────────────────┐
                  │ Refactor rules: Is order_size ≥ 4?        │
                  └─────────────────────┬─────────────────────┘
                                        │ Yes
                                        ▼
                                 ┌────────────┐
                                 │  RETURN    │
                                 │   TRUE     │ (Large order upsell)
                                 └────────────┘
                                        │
                                        │ No
                                        ▼
                     ┌────────────────────────────────────────────┐
                     │ Debugging challenge override: Is           │
                     │ temperature > 30 AND time_of_day == lunch  │
                     │ AND NOT loyalty_member?                     │
                     └───────────────────────┬────────────────────┘
                                             │ Yes
                                             ▼
                                      ┌────────────┐
                                      │  RETURN    │
                                      │   FALSE    │ (Busy lunch heatwave override)
                                      └────────────┘
                                             │
                                             │ No
                                             ▼
                         ┌───────────────────────────┐
                         │        RETURN FALSE        │
                         │     (Default – no upsell) │
                         └───────────────────────────┘
