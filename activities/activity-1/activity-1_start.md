## Step 0 – Create Your Notebook

1. In JupyterLab, click **File → New → Notebook**.  
2. Choose the Python 3 (ipykernel) kernel.  
3. Rename the new notebook to **Workshop3W_Master.ipynb** by right-clicking it in the explorer on the left and selected "Rename".
4. Modify the first cell in your notebook so that it's a Markdown cell. You can do this by clicking on the dropdown menu in the notebook tab command bar that says "Code" by default, then selecting "Markdown" from the menu.

**Add this as your first Markdown cell:**

    # Workshop 3W — Upsell Like an Engineer
    Unit 3 — Programming for Intelligent Products

    Today we’ll practise TDD (Red → Green → Refactor), experiment logging, and debugging discipline.

---

## Step 1 – Set Up Your Environment (then restart kernel)

**Cell 1 – Install packages**

Create a new Code cell and enter the following:

    !pip uninstall -y mlflow mlflow-skinny mlflow-tracing transformers || true
    !pip install "nvidia-ml-py3<8.0,>=7.352.0" "transformers<4.50,>=4.38.0" "mlflow==2.15.1" pandas scikit-learn
    print("Installed requirements. Please restart the kernel now.")

Verify this was successful by looking for the final output line `Installed requirements. Please restart the kernel now.`

*After* this runs, go to **Kernel → Restart Kernel**.

**Cell 2 – Verify**

Create another new Code cell:

    import sys, platform
    print("Python:", sys.version)
    print("Platform:", platform.platform())
    import mlflow, pandas as pd
    print("MLflow:", mlflow.__version__)
    print("Environment ready ✅")

Run this and ignore any warnings about deprecated packages. (In production code, you should pay attention to these and take action, but it's not vital today.)

Ensure that the MLflow version is 2.15.1 and you see `Environment ready ✅`.