# Behave + Playwright BDD Starter

This project is a small demo automation framework for learning and practicing behavior-driven testing. It combines:

- Behave for writing and running Gherkin-style scenarios
- Playwright for browser automation
- Streamlit for a simple UI to run features and inspect results
- Sample HTML pages and story documents to simulate a Jira-style workflow

## What this project contains

- features/: Gherkin feature files and step definitions
- pages/: Playwright page object classes for each page
- ui/: Streamlit app for running features from the browser
- app/: Sample local web pages used by the tests
- stories/: Markdown story files that map to features and pages
- relations.json: Mapping between stories, pages, features, and step files

## Prerequisites

- Python 3.9+
- A terminal with access to the project folder

## Setup

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

## Run the project

### Option 1: Start everything together
Run the helper script:

```bash
python start_app.py
```

This starts:
- the sample page server at http://127.0.0.1:8000
- the Streamlit UI at http://127.0.0.1:8501

### Option 2: Run Behave tests manually
Run all features:

```bash
python -m behave
```

Run one feature file:

```bash
python -m behave features/login.feature
```

Check steps without executing them:

```bash
python -m behave --dry-run
```

### Option 3: Run the Streamlit UI manually

```bash
python -m streamlit run ui/app.py --server.address 127.0.0.1 --server.port 8501
```

## Useful verification commands

Check Python syntax:

```bash
python -m py_compile ui/app.py
python -m py_compile pages/*.py
```

## Notes for interns

- Behave defines the business-readable scenarios.
- Playwright performs the browser actions.
- Streamlit gives a simple interface to run and inspect those scenarios.
- The sample app under app/ is used as the local target for the tests.
