Feature: Login page
  As a user
  I want to log in
  So that I can access my account

  Scenario: Show login feedback for valid credentials
    Given the login page is available
    When the user opens the login page
    And the user enters "jane@example.com" and "secret123"
    And the user submits the login form
    Then the login feedback should contain "Invalid credentials."

  Scenario: Show login feedback for a different valid user
    Given the login page is available
    When the user opens the login page
    And the user enters "alex@example.com" and "welcome123"
    And the user submits the login form
    Then the login feedback should contain "Invalid credentials."

  Scenario: Show login feedback for empty email
    Given the login page is available
    When the user opens the login page
    And the user enters "" and "secret123"
    And the user submits the login form
    Then the login feedback should contain "Email and password are required."

  Scenario: Show login feedback for empty password
    Given the login page is available
    When the user opens the login page
    And the user enters "jane@example.com" and ""
    And the user submits the login form
    Then the login feedback should contain "Email and password are required."

  Scenario: Show login feedback for invalid credentials
    Given the login page is available
    When the user opens the login page
    And the user enters "wrong@example.com" and "wrongpass"
    And the user submits the login form
    Then the login feedback should contain "Invalid credentials."
