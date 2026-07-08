Feature: Checkout page
  As a user
  I want to complete checkout
  So that I can place an order

  Scenario: Show checkout form feedback
    Given the checkout page is available
    When the user opens the checkout page
    And the user enters the shipping details for "Jane"
    And the user confirms the order
    Then the confirmation message should contain "Order confirmed"
