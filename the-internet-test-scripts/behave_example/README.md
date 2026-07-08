# Behave Fixture Example

This is the same dropdown test, but written in Behave style.

## Run

From the project root, with your environment activated:

```bash
behave the-internet-test-scripts/behave_example
```

Run without opening the browser window:

```bash
HEADLESS=true behave the-internet-test-scripts/behave_example
```

Run as a mobile browser:

```bash
MOBILE=true behave the-internet-test-scripts/behave_example
```

Run as a mobile browser without opening the browser window:

```bash
HEADLESS=true MOBILE=true behave the-internet-test-scripts/behave_example
```

Use a different Playwright device:

```bash
MOBILE=true DEVICE="iPhone 12" behave the-internet-test-scripts/behave_example
```

## What Is The Fixture Here?

In this example, these are the fixture-like objects:

```python
context.playwright
context.browser
context.page
```

They are created in `environment.py`.

## What Are Hooks?

Hooks are special Behave functions that run automatically.

```python
def before_all(context):
```

Runs once before all scenarios. Here we start Playwright and open the browser.

```python
def before_scenario(context, scenario):
```

Runs before every scenario. Here we open a fresh page.

```python
def after_scenario(context, scenario):
```

Runs after every scenario. Here we close the page.

```python
def after_all(context):
```

Runs once after all scenarios. Here we close the browser and stop Playwright.

## Network Calls

In `before_scenario`, this line listens to every network response:

```python
context.page.on("response", store_response)
```

Whenever the page loads HTML, CSS, JavaScript, images, or any other resource, Playwright calls `store_response`.

The code stores:

```text
method
url
status
resource_type
```

After each scenario, the network calls are saved here:

```text
the-internet-test-scripts/behave_example/artifacts/network/
```

## Reports

At the end of the run, `after_all` creates:

```text
the-internet-test-scripts/behave_example/artifacts/report.json
the-internet-test-scripts/behave_example/artifacts/report.md
```

The report contains:

```text
scenario name
pass/fail status
number of network calls
screenshot path
trace path
network log path
mobile true/false
```

Behave can also create its own JSON report:

```bash
behave the-internet-test-scripts/behave_example -f json -o the-internet-test-scripts/behave_example/artifacts/behave-report.json
```

## Playwright Trace Logs

Tracing is started before each scenario:

```python
context.browser_context.tracing.start(
    screenshots=True,
    snapshots=True,
    sources=True,
)
```

Tracing is stopped after each scenario:

```python
context.browser_context.tracing.stop(path=str(trace_path))
```

Trace files are saved here:

```text
the-internet-test-scripts/behave_example/artifacts/traces/
```

Open a trace with:

```bash
playwright show-trace the-internet-test-scripts/behave_example/artifacts/traces/select_option_1_from_dropdown.zip
```

If `playwright` is not available directly, use:

```bash
python -m playwright show-trace the-internet-test-scripts/behave_example/artifacts/traces/select_option_1_from_dropdown.zip
```

## Screenshots

After each scenario, this line saves a screenshot:

```python
context.page.screenshot(path=str(screenshot_path), full_page=True)
```

Screenshots are saved here:

```text
the-internet-test-scripts/behave_example/artifacts/screenshots/
```

## Mobile Screens

When you run with `MOBILE=true`, the hook uses a Playwright device:

```python
device_options = context.playwright.devices["Pixel 5"]
context.browser_context = context.browser.new_context(**device_options)
```

This changes the browser context to use mobile-like settings:

```text
mobile viewport
mobile user agent
touch support
device scale factor
```

That means the same Behave steps run against a mobile-sized browser.

## Flow

Behave runs this order:

```text
before_all
  before_scenario
    Given I open the dropdown page
    When I select "Option 1" from the dropdown
    Then the dropdown value should be "1"
  after_scenario
  before_scenario
    Given I open the dropdown page
    When I select "Option 2" from the dropdown
    Then the dropdown value should be "2"
  after_scenario
after_all
```

The step file uses `context.page`:

```python
context.page.goto("https://the-internet.herokuapp.com/dropdown")
```

That page was created earlier by `before_scenario`.
