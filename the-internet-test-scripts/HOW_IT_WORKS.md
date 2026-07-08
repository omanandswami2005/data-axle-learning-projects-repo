# How These Playwright Scripts Work

This folder contains simple Python Playwright automation scripts for testing common actions on:

https://the-internet.herokuapp.com/

Each file is a normal Python script. You can run one file at a time.

## Common Pattern

Every script follows this flow:

1. Import Playwright's synchronous Python API.
2. Open a Chromium browser.
3. Go to the required page on `the-internet.herokuapp.com`.
4. Perform one user action.
5. Check that the expected result appears on the page.
6. Print a success message.
7. Close the browser.

The scripts use:

```python
from playwright.sync_api import expect, sync_playwright
```

`sync_playwright()` starts Playwright.

`expect()` is Playwright's way to check that something happened correctly.

For example:

```python
expect(page.locator("xpath=//h3")).to_have_text("Dropdown List")
```

This means:

```text
Find the h3 heading and check that its text is Dropdown List.
```

## How XPath Is Used

In these scripts, elements are selected using relative XPath.

A relative XPath starts with `//`.

Example:

```python
page.locator("xpath=//button[normalize-space()='Click for JS Prompt']")
```

This means:

```text
Find any button on the page whose visible text is Click for JS Prompt.
```

The format is:

```python
page.locator("xpath=YOUR_XPATH_HERE")
```

Some useful XPath examples:

```python
page.locator("xpath=//h3")
page.locator("xpath=//select[@id='dropdown']")
page.locator("xpath=//input[@id='file-upload']")
page.locator("xpath=//button[normalize-space()='Click for JS Prompt']")
page.locator("xpath=//div[@id='uploaded-files']")
```

`@id='dropdown'` means:

```text
Find an element whose id is dropdown.
```

`normalize-space()='Click for JS Prompt'` means:

```text
Find an element by its visible text, ignoring extra spaces.
```

Relative XPath is usually better for practice than absolute XPath.

Good relative XPath:

```xpath
//input[@id='file-upload']
```

Avoid absolute XPath like this:

```xpath
/html/body/div[2]/div/div/form/input[1]
```

Absolute XPath breaks easily if the page structure changes.

## Browser Window

By default, the browser opens visibly:

```python
browser = playwright.chromium.launch(headless=is_headless(), slow_mo=300)
```

`slow_mo=300` slows actions down slightly so you can see what is happening.

To run without opening the browser window, use `HEADLESS=true`:

```bash
HEADLESS=true python the-internet-test-scripts/dropdown_test.py
```

## download_test.py

Target page:

```text
https://the-internet.herokuapp.com/download
```

What it does:

1. Opens the file download page.
2. Checks that the page title is `File Downloader`.
3. Finds the first downloadable file link.
4. Clicks the link.
5. Waits for the browser download event.
6. Saves the downloaded file into the local `downloads/` folder.
7. Confirms that the file exists locally.

Main Playwright line:

```python
first_file_link = page.locator("xpath=//div[contains(@class, 'example')]//a").first
```

This tells Playwright:

```text
Find the first download link inside the main example area.
```

## upload_test.py

Target page:

```text
https://the-internet.herokuapp.com/upload
```

What it does:

1. Opens the file upload page.
2. Checks that the page title is `File Uploader`.
3. Uploads `upload_sample.txt`.
4. Clicks the Upload button.
5. Confirms that the success page says `File Uploaded!`.
6. Confirms that the uploaded file name appears on the page.

Main Playwright line:

```python
page.locator("xpath=//input[@id='file-upload']").set_input_files(str(UPLOAD_FILE))
```

This tells Playwright which file to upload.

`upload_sample.txt` is just a simple text file in this folder. The script uploads that file.

## dropdown_test.py

Target page:

```text
https://the-internet.herokuapp.com/dropdown
```

What it does:

1. Opens the dropdown page.
2. Checks that the page title is `Dropdown List`.
3. Selects `Option 1`.
4. Verifies that the dropdown value is `1`.
5. Selects `Option 2`.
6. Verifies that the dropdown value is `2`.

Main Playwright line:

```python
dropdown = page.locator("xpath=//select[@id='dropdown']")
dropdown.select_option(label="Option 1")
```

This selects the dropdown option that says `Option 1`.

## modal_test.py

Target page:

```text
https://the-internet.herokuapp.com/entry_ad
```

What it does:

1. Opens the entry ad page.
2. Waits for the modal window to appear.
3. Checks that the modal title is `This is a modal window`.
4. Clicks `Close`.
5. Confirms that the modal is hidden.

The script also handles the case where the modal does not appear immediately. If that happens, it clicks `click here` to re-enable the modal and reloads the page.

Main Playwright lines:

```python
modal = page.locator("xpath=//div[@id='modal']")
expect(modal).to_be_visible(timeout=5000)
expect(modal).to_be_hidden()
```

These lines check that the modal first appears, and then disappears after clicking `Close`.

## prompt_test.py

Target page:

```text
https://the-internet.herokuapp.com/javascript_alerts
```

What it does:

1. Opens the JavaScript Alerts page.
2. Clicks `Click for JS Prompt`.
3. Handles the browser prompt dialog.
4. Enters custom text into the prompt.
5. Confirms that the result text appears on the page.

Main Playwright line:

```python
page.locator("xpath=//button[normalize-space()='Click for JS Prompt']").click()
```

This clicks the button using its visible text.

This line waits for the browser popup box:

```python
page.once("dialog", handle_dialog)
```

When the prompt appears, this line types text into it and clicks OK:

```python
dialog.accept(PROMPT_TEXT)
```

## Files In This Folder

```text
README.md
HOW_IT_WORKS.md
download_test.py
upload_test.py
dropdown_test.py
modal_test.py
prompt_test.py
upload_sample.txt
```

After running the download script, this folder may also contain:

```text
downloads/
```

## Recommended Run Order

```bash
python the-internet-test-scripts/dropdown_test.py
python the-internet-test-scripts/modal_test.py
python the-internet-test-scripts/prompt_test.py
python the-internet-test-scripts/upload_test.py
python the-internet-test-scripts/download_test.py
```

## Behave Fixture Example

There is also a small Behave example here:

```text
the-internet-test-scripts/behave_example/
```

Run it with:

```bash
behave the-internet-test-scripts/behave_example
```

In Behave, hooks inside `environment.py` create and clean up the shared objects.

The fixture-like objects are:

```python
context.playwright
context.browser
context.page
```

The hooks are:

```python
before_all
before_scenario
after_scenario
after_all
```

Simple way to remember:

```text
Hooks decide when setup/cleanup happens.
Fixtures are the prepared things you use in your steps.
```

The Behave example also shows:

```text
network call logs
Playwright trace files
screenshots
simple report files
mobile browser mode
```
