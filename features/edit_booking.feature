Feature: Edit a Booking
  In order to edit a booking
  As a user
  I want to edit a booking

  Background: There is a registered user and table
    Given Exists a user "user" with password "password"
    And Exists a table "table" with capacity 4

  Scenario: Edit a booking
    Given I login as user "user" with password "password"
    When I book a table
      | people_number | date       | time_zone     |
      | 4             | 30/05/2022 | 12:30 - 14:00 |
    Then There is 1 booking with time zone 1
    Then I edit the booking of a "booking"
      | time_zone     |
      | 14:00 - 15:30 |
    Then There is 1 booking with time zone 2
    Then I logout so there is login

