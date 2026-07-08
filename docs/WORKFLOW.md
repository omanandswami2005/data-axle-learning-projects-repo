# Workflow Overview

## How the pieces fit together

This project follows a simple BDD and POM flow:

1. Jira story or requirement is analyzed.
2. The story is converted into one or more BDD scenarios.
3. Each scenario is written in a feature file using Given / When / Then.
4. Step definitions map those human-readable steps to Python code.
5. The step code uses page objects to interact with the UI.
6. The page objects keep UI actions such as clicks, typing, and assertions in one place.

## Relationship diagram

```text
Jira Story / Requirement
        │
        ▼
BDD Scenario
        │
        ▼
Feature File (.feature)
        │
        ▼
Step Definitions (.py)
        │
        ▼
Page Object Model (POM)
        │
        ▼
Playwright UI Actions
```

## Simple example

```text
Story: User login
   ↓
Scenario: Valid user can sign in
   ↓
Feature file: Given the user is on the login page
               When the user enters valid credentials
               Then the dashboard is shown
   ↓
Step definition calls:
   - login_page.open()
   - login_page.enter_username()
   - login_page.enter_password()
   - login_page.click_login()
   ↓
Page object handles the UI interaction
```

## Important learning point

- A story describes what the user wants.
- A feature file describes the behavior in BDD form.
- A step definition connects the behavior to code.
- A page object contains the UI interaction logic.
- One story may use one page, many pages, or reuse the same page object across multiple stories.
