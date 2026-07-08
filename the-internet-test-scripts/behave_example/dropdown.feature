Feature: Dropdown page

  Scenario: Select option 1 from dropdown
    Given I open the dropdown page
    When I select "Option 1" from the dropdown
    Then the dropdown value should be "1"

  Scenario: Select option 2 from dropdown
    Given I open the dropdown page
    When I select "Option 2" from the dropdown
    Then the dropdown value should be "2"
