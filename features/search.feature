Feature: Search page
  As a user
  I want to search products
  So that I can find what I need

  Scenario: Show search results
    Given the search page is available
    When the user opens the search page
    And the user searches for "playwright"
    Then the search results should include "playwright"
