Feature: Add Address
  In order to add a new address
  As a user
  I want to add an address

  Background: There is a registered user
    Given Exists a user "user" with password "password"


  Scenario: Add an addres
    Given I login as user "user" with password "password"
    When I add an address
      | address_field                |
      | Rambla de Ferran, 32, Lleida |
    Then There is 1 address