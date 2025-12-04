# Welcome to Workshop 3 - Upsell Like an Engineer!

Hands-on workshop moving from exploratory notebooks to disciplined, professional Python for machine learning.

## Learning Intent

By the end of this workshop you will:

- Write code that is **testable**, **maintainable**, and **reproducible**  
- Practise **TDD** (Red → Green → Refactor) on a simple upsell predictor  
- **Log experiments** locally with MLflow  
- **Refactor** safely using tests as a safety net  
- Connect these habits to **risk reduction** and **technical debt**

## Notebook Guide (Single Notebook Flow)

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
This repo contains *one possible* solution for each activity. These are there to ensure that you're able to continue making progress throughout the workshop in the event that you become stuck or have technical difficulties at any stage. Please use them responsibly to supplement your learning, not to replace it. **These are not the only possible solution to each activity.** If you have logic that is passing the tests, it is a correct solution to the problem and you can proceed.

### Running Tests Locally

After completing the notebook, the final function lives in `src/hotdog/rules.py`.  
You can test it outside Jupyter like a real module.

Run from the terminal:

    PYTHONPATH=src pytest -q

or on Windows:

    set PYTHONPATH=src; pytest -q

This executes `tests/test_rules.py` and prints concise results (e.g. `6 passed in 0.04s`).

### MLflow Logging

MLflow acts as your digital lab notebook.

All runs are stored locally under:

    file:./mlruns

#### What Happens
1. Experiment “hotdog-upsell” is created or reused.  
2. Run “Initial Loyalty Rule” starts.  
3. Inputs and outputs are logged as parameters and metrics.  
4. A tag `rule_version=v1` is added for traceability.  

#### Safe Logging
If MLflow isn’t installed, `src/hotdog/logging_utils.py` prints:

    [INFO] MLflow not installed — skipping logging.

Enable it anytime with:

    pip install mlflow==2.15.1

#### Optional Script
Run the same logic outside Jupyter:

    PYTHONPATH=src python scripts/run_mlflow_example.py

## Going Further (Optional)

Export your notebook as a script for production pipelines.  
See [Convert notebook code into Python scripts – Azure Machine Learning (Microsoft Learn)](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-convert-ml-experiment-to-production?view=azureml-api-1)
