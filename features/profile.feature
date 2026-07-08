Feature: Profile page
  As a user
  I want to update my profile
  So that my account stays current

  Scenario: Show profile form message
    Given the profile page is available
    When the user opens the profile page
    And the user updates the profile name to "Jane Doe"
    Then the profile summary should contain "Jane Doe"
