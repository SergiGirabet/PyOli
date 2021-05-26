Feature: Update Backoffice
  In order to update an order
  As a superuser
  I want to change the status

  Background: There is a registered super user
    Given Exists a super user "user" with password "password"
    And Exists a product "product" with category "category"
    And Exists an address "address" by "user"
    #And Exists an order "order"

  Scenario: Update an order
    Given I login as user "user" with password "password"
    When I add a delivery
      | name       | quantity |
      | Sweet wine | 2        |
    Then The status of an order is PENDING
    Then I update the status
      | status    |
      | Preparing |
    Then The status of an order is PREPARING

