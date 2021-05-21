Feature: Add Product Order
  In order to have a delivery
  As a user
  I want to create a product order

  Background: There is a user, product with category and address
    Given Exists a user "user" with password "password"
    Given Exists a product "WhiteWine" with category "Premium"
    Given Exists an "order" by "user"


  Scenario: Add a Product Order
    Given I login as user "user" with password "password"
    When I create a delivery
      | ordered_product | date
      | WhiteWine       | 2021-05-18 20:17:16 |
    Then The new date of the booking is 2021-05-18 20:17:16
