Feature: Remove a Booking
  In order to remove a booking
  As a user
  I want to remove a booking

  Background: There is a registered user and table
    Given Exists a user "user" with password "password"
    And Exists a table "table" with capacity 4

  Scenario: Cancel the remove of a booking
    Given I login as user "user" with password "password"
    When I book a table
      | people_number | date       | time_zone     |
      | 4             | 30/05/2022 | 12:30 - 14:00 |
    Then I cancel the remove of a "booking"
    Then There is 1 booking

  Scenario: Remove a booking
    Given I login as user "user" with password "password"
    When I book a table
      | people_number | date       | time_zone     |
      | 4             | 30/05/2022 | 12:30 - 14:00 |
    Then I remove the "booking"
    Then There is 0 booking