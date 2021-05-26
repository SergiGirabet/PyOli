Feature: Add Delivery
  In order to add a new delivery
  As a user
  I want to make a delivery

  Background: There is a registered user
    Given Exists a user "user" with password "password"
    And Exists a product "product" with category "category"
    And Exists an address "address" by "user"


  Scenario: Add a delivery of a "product"
    Given I login as user "user" with password "password"
    When I add a delivery
      | name       | quantity |
      | Sweet wine | 2        |
    Then There is 1 delivery