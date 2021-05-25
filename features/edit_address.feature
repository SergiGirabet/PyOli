Feature: Edit an Address
  In order to edit a existing address
  As a user
  I want to edit an address

  Background: There is a registered user
    Given Exists a user "user" with password "password"


  Scenario: Edit an address
    Given I login as user "user" with password "password"
    When I add an address
      | address_field                |
      | Rambla de Ferran, 32, Lleida |
    Then There is 1 address with address Rambla de Ferran, 32, Lleida
    Then I edit the "address"
      | address_field                |
      | Avinguda Pius XII, 8, Lleida |
    Then There is 1 address with address Avinguda Pius XII, 8, Lleida


