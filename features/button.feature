Feature: Homepage call to action
  As a visitor
  I want to see the main action button
  So that I can interact with the sample UI

  Scenario: Display the primary button
    Given the sample app is available
    When the user opens the homepage
    Then the page should display the text "Start your test"
