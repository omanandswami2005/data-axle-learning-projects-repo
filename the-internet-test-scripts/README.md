# The Internet Playwright Scripts

Simple Python Playwright scripts for testing pages on:

https://the-internet.herokuapp.com/

## Run

From the project root:

```bash
python the-internet-test-scripts/download_test.py
python the-internet-test-scripts/upload_test.py
python the-internet-test-scripts/dropdown_test.py
python the-internet-test-scripts/modal_test.py
python the-internet-test-scripts/prompt_test.py
```

By default the browser opens visibly. To run headless:

```bash
HEADLESS=true python the-internet-test-scripts/dropdown_test.py
```

Downloaded files are saved in:

```text
the-internet-test-scripts/downloads/
```
