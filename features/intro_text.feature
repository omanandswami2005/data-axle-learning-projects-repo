Feature: Homepage intro text
  As a visitor
  I want to view the intro text on the page
  So that I can confirm the sample content is visible

  Scenario: Show the intro paragraph
    Given the sample app is available
    When the user opens the homepage
    Then the page should display the text "This page is used for the Behave + Playwright sample test."
