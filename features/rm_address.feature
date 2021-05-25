Feature: Remove an Address
  In order to remove a existing address
  As a user
  I want to remove an address

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Remove an address
    Given I login as user "user" with password "password"
    When I add an address
      | address_field                |
      | Rambla de Ferran, 32, Lleida |
    Then There is 1 address
    Then I cancel to delete the address "Rambla de Ferran, 32, Lleida"
    Then There is 1 address

  Scenario: Remove an address
    Given I login as user "user" with password "password"
    When I add an address
      | address_field                |
      | Rambla de Ferran, 32, Lleida |
    Then There is 1 address
    Then I delete the address "Rambla de Ferran, 32, Lleida"
    Then There is 0 address

