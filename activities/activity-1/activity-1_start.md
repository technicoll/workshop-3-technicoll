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