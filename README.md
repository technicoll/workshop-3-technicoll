# Welcome to Workshop 3 - Upsell Like an Engineer!

Hands-on workshop moving from exploratory notebooks to disciplined, professional Python for machine learning.

## Work on your own copy (Codespace recommended)
- **Preferred:** Fork this repository (or accept the GitHub Classroom link if provided), then create a Codespace from your fork. A Codespace gives you a ready-to-code cloud dev environment; learn more in the GitHub docs: https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces
- **Local option:** Clone the repo and work on your machine if you prefer.
- We’ll use the Python version that ships with your Codespace or local install (no explicit pin here).

![GitHub Codespaces diagram](https://docs.github.com/assets/cb-68851/mw-1440/images/help/codespaces/codespaces-diagram.webp)

## Python environment (venv)
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

## Requirements
Dependencies live in `requirements.txt` and match what you installed in the venv:
- mlflow==2.15.1
- pandas>=2.0.0
- scikit-learn>=1.3.0
- numpy>=1.24.0
- jupyter>=1.0.0
- ipykernel>=6.0.0
- pytest>=7.0.0

## MLflow (from an activated venv)
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

## Notebook guidance
- Create your notebook (none are in the repo yet). After activating the venv, use the “Select Kernel” button (top right in Jupyter) and choose the venv. 

## Learning intent

By the end of this workshop you will:

- Write code that is **testable**, **maintainable**, and **reproducible**  
- Practise **TDD** (Red → Green → Refactor) on a simple upsell predictor  
- **Log experiments** locally with MLflow  
- **Refactor** safely using tests as a safety net  
- Connect these habits to **risk reduction** and **technical debt**

## Notebook guide (single notebook flow)

We’ll work in **one Jupyter notebook** for the whole day.  
Follow the activities in order below and add one code cell at a time.

> **Tip:** Use Markdown headings inside your notebook to mirror these steps.

## Activities

You will work through activities in the [`activities` folder](/activities/) in order:
- [Activity 1: Environment Setup and Verification](/activities/activity-1/activity-1_start.md)
- [Activity 2: The First TDD Cycle (Red -> Green)](/activities/activity-2/activity-2_start.md)
- [Activity 3: The Second TDD Cycle & MLflow Logging](/activities/activity-3/activity-3_start.md)
- [Activity 4: The Refactoring Cycle](/activities/activity-4/activity-4_start.md)
- [Activity 5: The Debugging Challenge](/activities/activity-5/activity-5_start.md)
- [Activity 6: Git Simulation and Final Reflection](/activities/activity-6/activity-6_start.md)

## Help
### Solutions
This repo contains solutions for each activity. These are there to ensure that you're able to continue making progress throughout the workshop in the event that you become stuck or have technical difficulties at any stage. Please use them responsibly to supplement your learning, not to replace it.

### Running tests locally

After completing the notebook, the final function lives in `src/rules.py`.  
You can test it outside Jupyter like a real module (from an activated venv).

Run from the terminal:

    pytest -v

This executes `tests/test_rules.py` and prints concise results (e.g. `6 passed in 0.04s`).

## Going further (optional)

Move on to Activity 7 to bridge these habits into a small ML pipeline. Read `activities/activity-7/activity-7__start.md` for the overview: it maps pipeline stages to their tests and gives two focused exercises to harden preprocessing and keep accuracy guardrails. Apply the same TDD + defensive + observability mindset you used here. You’ll fork and open a Codespace on the testing mini-project repo you used in Aptem Module 3.1 (https://github.com/corndel-ai/testing-mini-project); if you’ve done it before, you can repeat the core tasks or jump to the further exercises.
