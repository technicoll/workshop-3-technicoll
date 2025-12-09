# Bridging Workshop 3 and the Mini Testing Project in Aptem

This bridge keeps one idea front and centre, TDD, defensive, and observability habits you practiced on a pure function now apply to an pipeline. Below: (1) the pipeline stages mapped to the exact tests that cover them, and (2) two focused exercises to extend the project.

In the Aptem module *3.1 Python Essentials for AI enginers* e-learning, if you compelted this you saw how `.py` modules and automated tests underpin long-term maintainability. Here, we can reinforce that with automated tests and version control act as living documentation of what last worked, and TDD is how you keep that truth current.

> This exercise builds directly on the Aptem e-learning “31. Python Essentials for AI Engineers”. You were given a worked solution in that module; use it as your baseline here.

---

## Prerequisites

Before starting these exercises, ensure you have:

- ✅ **Completed Workshop 3W exercises** (TDD basics, pure functions, red-green-refactor cycle)
- ✅ **Forked and opened a Codespace on the testing mini-project repo** you used in Aptem Module 3.1: https://github.com/corndel-ai/testing-mini-project (if you’ve done it before, you can repeat or jump to the further exercises)
- ✅ **Virtual environment activated** and dependencies installed in that repo (use your venv name; `.venv` shown here):
  ```bash
  python -m venv .venv
  # Activate
  source .venv/bin/activate  # macOS/Linux
  # Windows: .\.venv\Scripts\activate
  pip install -r requirements.txt
  ```
- ✅ **All tests currently passing**:
  ```bash
  pytest tests/ -v
  # Expected output: All tests pass (should see 4 passed)
  ```
- ✅ **Familiarity with project structure** (review `README.md` if needed)

---

## Pipeline → Tests Map (files and paths)

Understanding how each pipeline stage is tested helps you extend the project systematically.

- **Preprocess (`preprocess_text`)**
  - **Function**: Lowercases, strips non-alpha, collapses spaces.
  - **Tests**: [tests/test_TextClassifier_unit.py](../tests/test_TextClassifier_unit.py) (basic normalization; you'll extend this in Exercise 1).
  - **Current coverage**: Mixed case, empty strings
  - **TODO items**: Lines 8-12 contain 5 test cases you'll implement

- **Vectorize + Train (`train`)**
  - **Function**: `CountVectorizer.fit_transform` on training texts; `LogisticRegression.fit` on features/labels.
  - **Tests**: [tests/conftest.py](../tests/conftest.py) (session-scoped fixture trains on [data/raw/text-label.csv](../data/raw/text-label.csv) and returns `trained_classifier`).
  - **Why a fixture**: Training once per test session (not per test) speeds up the suite 3x.

- **Predict (`predict`)**
  - **Function**: Preprocess → `vectorizer.transform` → `model.predict`; critically, **no fitting**.
  - **Tests**:
    - [tests/test_TextClassifier_integration.py](../tests/test_TextClassifier_integration.py) - End-to-end accuracy threshold (≥65%) on unseen inputs
    - [tests/test_TextClassifier_regression.py](../tests/test_TextClassifier_regression.py) - Performance guardrail (≥80%) on clear examples
  - **Key insight**: Integration tests verify the pipeline works; regression tests ensure it doesn't get worse over time.

- **Evaluate (`evaluate`)**
  - **Function**: Wraps `predict` + `accuracy_score`.
  - **Tests**: [tests/test_TextClassifier_regression.py](../tests/test_TextClassifier_regression.py) (calls `evaluate` to enforce accuracy ≥ threshold).
  - **ML-specific testing**: Unlike deterministic functions, ML tests use thresholds, not exact values.

- **Split (caller responsibility in `app.py`)**
  - **Function**: `train_test_split` isolates training/test data.
  - **Tests**: None direct; usage demonstrated in [app.py](../app.py) (train on `X_train/y_train`, evaluate on `X_test/y_test`) to avoid leakage.

---

## Exercise 1: Complete the TODO Tests (TDD Foundation)

**Goal**: Reuse the Aptem e-learning test suite (from “31. Python Essentials for AI Engineers”) by dropping it into [tests/test_TextClassifier_unit.py](../tests/test_TextClassifier_unit.py). This is the same suite you were given; use it as your baseline.

**Time**: 20-30 minutes

**Why this matters**: The current `preprocess_text` implementation ([src/TextClassifier.py](../src/TextClassifier.py#L25-L37)) is intentionally basic. Production text preprocessing must handle edge cases: punctuation, multiple spaces, numbers, symbols. These TODOs guide you to harden it systematically using the TDD approach from Workshop 3W.

---

### Step 1: Drop in the reference tests

Paste the Aptem reference tests into `tests/test_TextClassifier_unit.py` (replace the TODO comments), directly below `test_preprocess_text_empty()`:

```python
from src.TextClassifier import TextClassifier


def test_preprocess_text_basic():
    """Unit test for basic text preprocessing."""
    classifier = TextClassifier()
    assert classifier.preprocess_text("HELLO WORLD") == "hello world"
    # Test case for mixed case text
    assert classifier.preprocess_text("PYthon is FUN") == "python is fun"
    # Test case for punctuation removal
    assert classifier.preprocess_text("Hello, World!") == "hello world"
    # Test case for numbers and symbols
    assert (
        classifier.preprocess_text("Numbers 123 and symbols!@#")
        == "numbers and symbols"
    )
    # Test case for leading/trailing spaces and multiple spaces
    assert (
        classifier.preprocess_text("  leading and trailing spaces  ")
        == "leading and trailing spaces"
    )
    # Test case for multiple spaces between words
    assert (
        classifier.preprocess_text("text with    multiple   spaces")
        == "text with multiple spaces"
    )


def test_preprocess_text_empty():
    """Unit test for empty string preprocessing."""
    classifier = TextClassifier()
    assert classifier.preprocess_text("") == ""
```

**TDD Principle**: Keep tests as your source of truth. If they fail, fix the implementation; if they pass, you’ve documented the behavior.

---

### Step 3: Run just the unit tests and observe results (🔴 RED)

```bash
pytest tests/test_TextClassifier_unit.py -v
```

**Expected output**: If your `preprocess_text` matches the e-learning solution, many or all tests may already pass. If any fail, that’s your cue to tighten `preprocess_text()` in [src/TextClassifier.py](../src/TextClassifier.py) until they’re green.

---

### Step 4: Verify implementation (🟢 GREEN PHASE)

The current implementation should take care of all these cases:

```python
def preprocess_text(self, text: str) -> str:
    """Cleans and normalizes a single text string."""
    text = text.lower()  # Handles mixed case ✓
    non_alphabetical_characters = r"[^a-z\s]"
    text = re.sub(non_alphabetical_characters, "", text)  # Removes punctuation, numbers ✓
    text = " ".join(text.split())  # Collapses spaces ✓
    return text
```

**Analysis**:
- `text.lower()` → Handles **mixed case** ✓
- `re.sub(r"[^a-z\s]", "", text)` → Removes **punctuation, numbers, symbols** ✓
- `" ".join(text.split())` → Removes **leading/trailing spaces** and **collapses multiple spaces** ✓

If any test fails, debug which assertion failed and adjust the implementation.

---

### Step 5: Ensure full test suite still passes

Your changes to unit tests shouldn't break integration or regression tests:

```bash
pytest tests/ -v
```

**Expected output**:
```
tests/test_TextClassifier_integration.py::test_end_to_end_pipeline_integration PASSED                                                                                   [ 25%]
tests/test_TextClassifier_regression.py::test_model_regression_accuracy PASSED                                                                                          [ 50%]
tests/test_TextClassifier_unit.py::test_preprocess_text_basic PASSED                                                                                                    [ 75%]
tests/test_TextClassifier_unit.py::test_preprocess_text_empty PASSED                                                                                                    [100%]
```

**Success criteria**: 100% of tests pass.

---

**🎓 Exercise 1 Complete!** You've successfully:
- ✅ Verified the e-learning tests work with the current implementation
- ✅ Confirmed unit tests in isolation
- ✅ Confirmed integration/regression tests still pass (system-level health check)

**This confirms the baseline works. Now let's practice real TDD by adding tests that FAIL first.**

---

## Exercise 1b: TDD in Action — Write Failing Tests First (🔴 RED → 🟢 GREEN)

**Goal**: Experience true TDD by adding tests for features the current `preprocess_text` does NOT handle. You'll see tests fail (RED), then update the implementation to make them pass (GREEN).

**Time**: 25-35 minutes

**Why this matters**: The current implementation is intentionally limited. Real-world text data contains HTML tags, URLs, and accented characters. This exercise shows how TDD drives feature development—you write the test first, watch it fail, then implement the fix.

---

### Step 1: Add the failing tests (🔴 RED PHASE)

Add these new test functions to the **end** of `tests/test_TextClassifier_unit.py`:

```python
# =============================================================================
# TDD EXERCISE: The following tests will FAIL with the current implementation.
# Students must update src/TextClassifier.py to make them pass.
# =============================================================================


def test_preprocess_text_html_tags():
    """TDD Exercise: HTML tags should be removed from text."""
    classifier = TextClassifier()
    assert classifier.preprocess_text("<p>Hello</p>") == "hello"
    assert classifier.preprocess_text("<div>Some <b>bold</b> text</div>") == "some bold text"
    assert classifier.preprocess_text("No tags here") == "no tags here"


def test_preprocess_text_urls():
    """TDD Exercise: URLs should be removed from text."""
    classifier = TextClassifier()
    assert classifier.preprocess_text("Visit https://example.com today") == "visit today"
    assert classifier.preprocess_text("Check http://test.org for info") == "check for info"
    assert classifier.preprocess_text("No URLs here") == "no urls here"


def test_preprocess_text_accented_characters():
    """TDD Exercise: Accented characters should be normalized to ASCII."""
    classifier = TextClassifier()
    assert classifier.preprocess_text("café") == "cafe"
    assert classifier.preprocess_text("résumé") == "resume"
    assert classifier.preprocess_text("naïve") == "naive"
    assert classifier.preprocess_text("El Niño") == "el nino"
```

---

### Step 2: Run tests and confirm they fail (🔴 RED)

```bash
pytest tests/test_TextClassifier_unit.py -v
```

**Expected output**: You should see **3 failing tests**:

```
tests/test_TextClassifier_integration.py::test_end_to_end_pipeline_integration PASSED                                            [ 14%]
tests/test_TextClassifier_regression.py::test_model_regression_accuracy PASSED                                                   [ 28%]
tests/test_TextClassifier_unit.py::test_preprocess_text_basic PASSED                                                             [ 42%]
tests/test_TextClassifier_unit.py::test_preprocess_text_empty PASSED                                                             [ 57%]
tests/test_TextClassifier_unit.py::test_preprocess_text_html_tags FAILED                                                         [ 71%]
tests/test_TextClassifier_unit.py::test_preprocess_text_urls FAILED                                                              [ 85%]
tests/test_TextClassifier_unit.py::test_preprocess_text_accented_characters FAILED                                               [100%]
```

**Why do they fail?** Let's analyze:

| Test | Input | Current Output | Expected | Problem |
|------|-------|---------------|----------|----------|
| HTML tags | `<p>Hello</p>` | `phellop` | `hello` | Tags treated as letters |
| URLs | `Visit https://example.com` | `visit httpsexamplecom` | `visit` | URL not removed |
| Accents | `café` | `caf` | `cafe` | Accented `é` removed entirely |

**This is TDD in action!** The tests define the behavior we want. Now we implement it.

---

### Step 3: Update `preprocess_text` to pass all tests (🟢 GREEN PHASE)

Open `src/TextClassifier.py` and replace the `preprocess_text` method with this enhanced version:

```python
def preprocess_text(self, text: str) -> str:
    """
    Cleans and normalizes a single text string.
    - Removes HTML tags
    - Removes URLs
    - Normalizes accented characters to ASCII
    - Lowercases text
    - Removes non-alphabetic characters (keeping spaces)
    - Collapses multiple spaces
    """
    import unicodedata

    logging.debug(f"Preprocessing text: '{text}'")

    # Step 1: Remove HTML tags (before lowercasing to handle <P> vs <p>)
    text = re.sub(r"<[^>]+>", "", text)

    # Step 2: Remove URLs (http, https, www)
    text = re.sub(r"https?://\S+|www\.\S+", "", text)

    # Step 3: Lowercase
    text = text.lower()

    # Step 4: Normalize accented characters to ASCII (é → e, ñ → n)
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("utf-8")

    # Step 5: Remove non-alphabetical characters (keeping spaces)
    non_alphabetical_characters = r"[^a-z\s]"
    text = re.sub(non_alphabetical_characters, "", text)

    # Step 6: Collapse multiple spaces and trim
    text = " ".join(text.split())

    logging.debug(f"Preprocessed text: '{text}'")
    return text
```

**Key additions explained**:

1. **HTML removal**: `re.sub(r"<[^>]+>", "", text)` matches anything between `<` and `>`
2. **URL removal**: `re.sub(r"https?://\S+|www\.\S+", "", text)` matches http/https URLs
3. **Accent normalization**: `unicodedata.normalize("NFKD", ...)` decomposes `é` into `e` + combining accent, then `encode("ascii", "ignore")` drops the accent

---

### Step 4: Run tests again — all should pass (🟢 GREEN)

```bash
pytest tests/test_TextClassifier_unit.py -v
```

**Expected output**:

```
tests/test_TextClassifier_unit.py::test_preprocess_text_basic PASSED
tests/test_TextClassifier_unit.py::test_preprocess_text_empty PASSED
tests/test_TextClassifier_unit.py::test_preprocess_text_html_tags PASSED
tests/test_TextClassifier_unit.py::test_preprocess_text_urls PASSED
tests/test_TextClassifier_unit.py::test_preprocess_text_accented_characters PASSED

========================= 5 passed in 0.15s =========================
```

🎉 **All tests pass!**

---

### Step 5: Verify full test suite still passes

Ensure your changes don't break integration or regression tests:

```bash
pytest tests/ -v
```

**Expected**: All tests pass (unit + integration + regression).

---

### 🤔 Puzzler: Does Accent Normalization Actually Help?

We just implemented `café` → `cafe`. But pause and think:

> **Would normalising accents actually improve classification accuracy?**

Consider:
- If your training data contains `"café"` and test data contains `"cafe"`, they'd be treated as different words without normalization. So normalization **helps** by unifying them.
- But if your training data is mostly English and rarely contains accented words, does it matter?
- What if you're classifying French or Spanish text where accents carry meaning? (`"résumé"` vs `"resume"` mean different things!)

**The lesson**: Text preprocessing isn't about "cleaning" for its own sake—it's about making your model more accurate. Every preprocessing step should be justified by asking: *"Does this help the model generalize better?"*

This is why we test—if normalisation hurts accuracy on your specific dataset, your regression tests will catch it.

---

## Exercise 1c: Research Challenge — Repeated Characters (Independent TDD)

**Goal**: Apply TDD independently by writing a failing test, then researching and implementing the solution yourself.

**Time**: 20-30 minutes

**Why this matters**: In the real world, you won't always have a solution handed to you. This exercise simulates that experience—you define the behavior with a test, then figure out how to implement it.

---

### The Challenge: Normalize Repeated Characters

Social media and informal text often contains exaggerated spelling for emphasis:
- `"sooooo good"` → should become `"so good"`  
- `"yessss"` → should become `"yes"`
- `"hellloooo"` → should become `"helo"` (or `"hello"` depending on your approach)

**Why does this matter for classification accuracy?**

Imagine your training data contains `"good"` labelled as positive sentiment. At prediction time, someone writes `"goooood"`—without normalization, the model sees this as an unknown word and can't use what it learned about `"good"`. By collapsing repeated characters, `"goooood"` becomes `"good"` (or `"god"`), letting the model recognize it.

> **Key insight**: Preprocessing should help the model generalize from training data to real-world input. Repeated character normalisation bridges informal text back to the vocabulary the model learned.

Your task: Add a test that fails, then research how to fix it.

---

### Step 1: Add the failing test (🔴 RED)

Add this test to the end of `tests/test_TextClassifier_unit.py`:

```python
def test_preprocess_text_repeated_characters():
    """Research Challenge: Repeated characters should be collapsed."""
    classifier = TextClassifier()
    # Repeated characters should be reduced (at minimum to 2, ideally to 1)
    assert classifier.preprocess_text("sooooo") == "so"
    assert classifier.preprocess_text("yessss") == "yes"
    assert classifier.preprocess_text("goooood") == "god"  # or "good" - your choice!
    assert classifier.preprocess_text("normal text") == "normal text"  # unchanged
```

---

### Step 2: Confirm the test fails

```bash
pytest tests/test_TextClassifier_unit.py::test_preprocess_text_repeated_characters -v
```

You should see output like:
```
AssertionError: assert 'sooooo' == 'so'
```

---

### Step 3: Research and implement (🟢 GREEN) — YOU figure this out!

**Hints**:
- 🔍 Search: "python regex repeated characters"
- 🔍 Search: "regex backreference"
- 🔍 The pattern involves capturing a character and matching when it repeats
- 🤖 And of course we could ask a chatbot for a solution! However, it's still good practice to find online offical guides to validate what chatbots tell us.

**Things to consider**:
- Where in `preprocess_text` should this step go?
- Should you reduce to 1 character or 2? (e.g., `"goood"` → `"god"` or `"good"`?)
- How do you handle legitimate double letters like `"good"` or `"book"`?

**Classic and authoritaive Resources for this exercise**:
- [Python `re` module documentation](https://docs.python.org/3/library/re.html)
- [Regex101](https://regex101.com/) — test your regex patterns interactively

---

### Step 4: Verify your solution

```bash
pytest tests/test_TextClassifier_unit.py -v
```

All tests should pass, including your new one.

---

### Step 5: Reflect

Once you've solved it, consider:
- Was reducing to 1 character the right choice? What breaks?
- Would reducing to 2 characters be safer? (e.g., `"goood"` → `"good"`)
- How would you handle edge cases like `"aaa"` or single-letter words?

**Note**: There's no single "correct" answer—different NLP tasks require different approaches. The important thing is that your test documents your decision.

---

**🎓 Exercise 1c Complete!** You've:
- ✅ Written a test without a provided solution
- ✅ Researched regex patterns independently
- ✅ Made design decisions about edge cases
- ✅ Practiced the full TDD cycle with minimal guidance

**This is what real-world TDD feels like—tests define behavior, implementation requires research.**

---

## Exercise 2: Add Experiment Tracking with MLflow

**Goal**: Instrument your training pipeline with MLflow to track experiments, then make a change and compare results.

**Time**: 15-20 minutes

**Why this matters**: In Workshop 3 you have logged function calls to observe behaviour. In ML, you log *experiments*—each model training run with its hyperparameters and results. This lets you answer questions like "Did changing max_iter from 1000 to 2000 improve accuracy?"

---

### Step 1: Add MLflow to dependencies

Edit [requirements.txt](../requirements.txt) and add:

```
mlflow==2.15.1
setuptools
```

Then install (make sure your venv is activated):

```bash
source venv/bin/activate  # if not already activated
pip install -r requirements.txt
```

---

### Step 2: Instrument the `train` method with MLflow logging

Open [src/TextClassifier.py](../src/TextClassifier.py) and replace the `train` method with this version that tracks both **hyperparameters** and **accuracy**:

```python
def train(self, texts: list[str], labels: list[str]):
    """Trains the classification model with MLflow experiment tracking."""
    logging.info("Starting model training.")

    # Preprocess and vectorize
    processed_texts = [self.preprocess_text(text) for text in texts]
    X = self.vectorizer.fit_transform(processed_texts)
    y = labels

    # Train the model
    self.model.fit(X, y)

    # Calculate training accuracy
    train_accuracy = self.model.score(X, y)

    # ---- MLflow experiment tracking ----
    try:
        import mlflow
        mlflow.set_tracking_uri("file:./mlruns")
        mlflow.set_experiment("text-classifier")

        with mlflow.start_run():
            # Log hyperparameters (what we configured)
            mlflow.log_param("max_iter", self.model.max_iter)
            mlflow.log_param("model_type", type(self.model).__name__)
            mlflow.log_param("vectorizer_type", type(self.vectorizer).__name__)

            # Log metrics (what resulted)
            mlflow.log_metric("train_samples", len(texts))
            mlflow.log_metric("vocab_size", len(self.vectorizer.vocabulary_))
            mlflow.log_metric("train_accuracy", train_accuracy)

    except Exception as e:
        logging.info(f"MLflow logging skipped: {e}")

    logging.info(f"Model training completed. Training accuracy: {train_accuracy:.4f}")
```

**What we're logging**:
- **Parameters**: `max_iter`, model type, vectorizer type (the choices we made)
- **Metrics**: Training samples, vocabulary size, and **training accuracy** (the results)

Now when you compare runs in MLflow UI, you'll see how accuracy changes with different hyperparameters!

---

### Step 3: Run the baseline experiment

```bash
python app.py
```

This trains the model and logs the first experiment to MLflow. Note the output accuracy.

> ⚠️ **Note on accuracy**: You'll likely see `train_accuracy: 1.0` (100%) in your MLflow runs. This is because our toy dataset is very small (16 samples) with clearly distinct positive/negative examples—the model easily memorizes it perfectly. Don't worry! The value of this exercise isn't seeing accuracy change—it's **learning the MLflow workflow**: tracking parameters, logging metrics, and comparing runs. In a real project with hundreds or thousands of samples, you'd see meaningful differences when tuning hyperparameters.

---

### Step 4: Make a change to the model

Open [src/TextClassifier.py](../src/TextClassifier.py) and modify the `__init__` method:

**Change this**:
```python
self.model = LogisticRegression(max_iter=1000)
```

**To this**:
```python
self.model = LogisticRegression(max_iter=2000)  # Increased iterations
```

Save the file.

---

### Step 5: Run the modified experiment

```bash
python app.py
```

This trains the model again with the new hyperparameter and logs a second experiment. Note if accuracy changed.

---

### Step 6: Launch MLflow UI and compare runs

First, make sure your venv is activated, then launch the UI:

```bash
source venv/bin/activate  # if not already activated
mlflow ui --port 5000 --backend-store-uri file:./mlruns
```

**Open your browser**: http://localhost:5000

You should see:
- **Experiments table**: Two runs with different `max_iter` values
- **Columns**: Start time, parameters (max_iter: 1000 vs 2000), metrics (accuracy, vocab_size)

**To compare**:
1. Select both runs (checkboxes)
2. Click **"Compare"** button
3. See side-by-side differences in parameters and metrics

**Questions to explore**:
- Did increasing `max_iter` change accuracy?
- Is vocabulary size the same? (It should be—vocab doesn't depend on model training)
- How long did each run take?

> 💡 **Tip**: You can also explore the `mlruns/` directory directly to see how MLflow stores data:
> ```bash
> tree mlruns/ -L 3
> ```
> Each run is stored as a folder with `params/`, `metrics/`, and `tags/` subdirectories containing plain text files. This makes MLflow data easy to inspect, version control, or back up.

---

### Step 7: Experiment freely (optional)

Try other changes and observe in MLflow:

**A. Change regularization**:
```python
self.model = LogisticRegression(max_iter=1000, C=0.5)  # Stronger regularization
```

**B. Try a different model**:
```python
from sklearn.svm import LinearSVC
self.model = LinearSVC(max_iter=1000)
```

Each change creates a new run in MLflow. You can compare all of them to see what works best for your data.

---

**🎓 Exercise 2 Complete!** You've:
- ✅ Instrumented code with MLflow experiment tracking
- ✅ Run multiple experiments with different configurations
- ✅ Used MLflow UI to compare results visually
- ✅ Applied Workshop 3's observability habit to ML experimentation

**This shows how logging in ML differs from logging function calls—you log entire experiments, not individual operations.**

**Congratulations!** You've bridged pure-function TDD to *stateful* ML pipelines (pipelines that keep and transform data across multiple steps). The habits you practiced in Workshop 3, writing tests first, then observing behaviour, now apply to machine learning systems.

---

## Going Further: Ideas for Exploration

You've completed the core bridge exercises. Here are directions you could explore next:

### Feature Engineering

- **Try TF-IDF**: Replace `CountVectorizer()` with `TfidfVectorizer()`
  - Downweights common words like "the", "is"
  - Often improves accuracy by 5-15%

- **Add bigrams**: `CountVectorizer(ngram_range=(1, 2))`
  - Captures phrases like "not good" (different from "good")
  - Compare with/without using MLflow

**Why not test these?** You'd be testing sklearn's implementation, not your code. Instead, use MLflow to compare performance—that's the ML way of validation.

### Model Improvements

- **Try different classifiers**: `LinearSVC`, `RandomForestClassifier`, `MultinomialNB`
- **Tune hyperparameters**: Vary `C` in LogisticRegression, try different solvers
- **Cross-validation**: Use `cross_val_score` for more robust accuracy estimates

Track everything in MLflow and compare which combinations work best!
