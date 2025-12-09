## Expected outputs
You'll create a Jupyter Notebook in your Codespace or local environment (using the venv you set up from the README). You'll verify the environment so you're ready to progress with the rest of the workshop. By the end, you'll have:
- One Markdown cell.
- Two Code cells that you've successfully run.

## Step 0 – Setup your environment and create your notebook
### 1. Setup environment
#### Work on your own copy (Codespace recommended)
- **Preferred:** Fork this repository (or accept the GitHub Classroom link if provided), then create a Codespace from your fork. A Codespace gives you a ready-to-code cloud dev environment; learn more in the GitHub docs: https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces
- **Local option:** Clone the repo and work on your machine if you prefer.
- We’ll use the Python version that ships with your Codespace or local install (no explicit pin here).

![GitHub Codespaces diagram](https://docs.github.com/assets/cb-68851/mw-1440/images/help/codespaces/codespaces-diagram.webp)

#### Python environment (venv)
We recommend running all workshop exercises in a Python virtual environment, just as you did in Aptem Module 3.1 (automated tests) and the testing-mini-project (https://github.com/corndel-ai/testing-mini-project).

- Create and activate a venv (macOS/Linux):
  - `python -m venv .venv`
  - `source .venv/bin/activate`
- Windows:
  - `python -m venv .venv`
  - `.\\.venv\\Scripts\\activate`
- Upgrade pip and install dependencies:
  - `python -m pip install --upgrade pip`
  - `pip install -r requirements.txt`

> “A virtual environment is a directory that contains a Python installation for a particular version of Python, plus a number of additional packages.” — [Real Python: Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)

#### Requirements
Dependencies live in `requirements.txt` and match what you installed in the venv:
- mlflow==2.15.1
- pandas>=2.0.0
- scikit-learn>=1.3.0
- numpy>=1.24.0
- jupyter>=1.0.0
- ipykernel>=6.0.0
- pytest>=7.0.0

#### MLflow (from an activated venv)
MLflow is commonly used to track model-training experiments, but here we use it early to show how it can log any action we choose in a clear, auditable way.

- Run the UI in the foreground (defaults to local paths like `./mlruns`):
  - `mlflow ui --port 5000 --backend-store-uri file:./mlruns`
  - Open http://localhost:5000
- Run in the background with logs:
  - `nohup mlflow ui --port 5000 --backend-store-uri file:./mlruns > mlflow.log 2>&1 &`
  - `echo $! > mlflow.pid`
  - Tail logs: `tail -f mlflow.log`
- Stop/inspect:
  - `kill $(cat mlflow.pid)` (or `pkill -f "mlflow ui"` if needed)
  - `lsof -i :5000` to confirm it stopped
- Run the sample script from the repo root:
  - `PYTHONPATH=src python scripts/run_mlflow_example.py`

### 2. Create notebook
1. Make sure you’ve created and activated the venv per the section above, and installed dependencies with `pip install -r requirements.txt` (repeat here for completeness).
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
