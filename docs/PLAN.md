# Manual Test Framework Plan

## Objective
Build a Python-based BDD test framework that can take Jira stories and requirement details, turn them into clear test scenarios, inspect the application UI, map scenarios to UI elements, reuse existing automation steps, and generate feature files with matching step implementations.

## Scope for This Phase
- Keep the workflow manual for now.
- Focus on structure, process, and reusable patterns.
- Do not implement AI prompting or autonomous agents yet.

## Proposed Approach
1. Understand the Jira story
   - Read the story title, description, acceptance criteria, and business rules.
   - Extract functional behavior, validations, edge cases, and negative paths.

2. Convert the story into BDD scenarios
   - Write scenarios in Given / When / Then format.
   - Cover happy path, edge cases, and validation failures.

3. Inspect the UI
   - Review the target application and identify page elements relevant to the scenarios.
   - Capture DOM structure, selectors, and interaction points.

4. Map scenarios to UI actions
   - Connect each scenario step to a UI action such as click, input, select, verify text, or assertion.
   - Identify reusable actions and shared page interactions.

5. Analyze the current automation framework
   - Review existing step definitions, page objects, utilities, and locators.
   - Reuse existing components wherever possible.

6. Generate feature files and step implementations
   - Create or update feature files using the agreed BDD style.
   - Implement step definitions that align with the current framework structure.

## Suggested Tech Stack
- Python
- Playwright for browser automation
- pytest-bdd or behave for BDD execution
- Page Object Model for UI interactions
- JSON/YAML for data-driven examples if needed

## Recommended Project Structure
```text
project/
  features/
    example.feature
  steps/
    test_steps.py
  pages/
    base_page.py
    login_page.py
    dashboard_page.py
  locators/
    login_locators.py
  utils/
    helpers.py
    config.py
  data/
    test_data.json
  tests/
    conftest.py
```

## Milestones
### 1. Foundation Setup
- Create the Python project structure.
- Install Playwright and BDD dependencies.
- Configure browser execution and basic test runner setup.

### 2. Story-to-Scenario Mapping
- Create a template for converting Jira stories into BDD scenarios.
- Define how to capture acceptance criteria and edge cases.

### 3. UI Inspection and Element Mapping
- Identify key pages and DOM elements.
- Document selectors and reusable UI actions.

### 4. Framework Alignment
- Review existing step definitions and page objects.
- Standardize naming and structure for future scenarios.

### 5. Feature File Generation
- Create feature files for sample stories.
- Implement step definitions that fit the current framework.

### 6. Validation and Execution
- Run the generated scenarios.
- Fix gaps between scenarios, steps, and UI implementation.

## Deliverables
- One working BDD feature file for a sample Jira story
- Matching step implementation using the current framework style
- A reusable pattern for future story-to-feature conversion
- A simple document outlining how to inspect UI elements and map them to scenarios

## Definition of Done
The initial phase is complete when:
- A sample Jira story can be translated into BDD scenarios.
- A feature file exists for that story.
- Step definitions are implemented and runnable.
- The structure is clear enough to repeat for future stories.
