Feature: Password reset page
  As a user
  I want to reset my password
  So that I can regain access

  Scenario: Show reset form message for a valid email
    Given the password reset page is available
    When the user opens the password reset page
    And the user submits the password reset form for "jane@example.com"
    Then the reset status should contain "Password reset"

  Scenario: Show reset form message for another valid email
    Given the password reset page is available
    When the user opens the password reset page
    And the user submits the password reset form for "alex@example.com"
    Then the reset status should contain "Password reset"

  Scenario: Show reset form message for empty email
    Given the password reset page is available
    When the user opens the password reset page
    And the user submits the password reset form for ""
    Then the reset status should contain "Please enter your email"

  Scenario: Show reset form message for an invalid format
    Given the password reset page is available
    When the user opens the password reset page
    And the user submits the password reset form for "not-an-email"
    Then the reset status should contain "Please enter a valid email"

  Scenario: Show reset form message for a missing account
    Given the password reset page is available
    When the user opens the password reset page
    And the user submits the password reset form for "ghost@example.com"
    Then the reset status should contain "No account found"
