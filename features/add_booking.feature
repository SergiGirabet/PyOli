Feature: Add Booking
  In order to book a table
  As a user
  I want to add a book

  Background: There is a registered user and table
    Given Exists a user "user" with password "password"
    And Exists a table "table" with capacity 4

  Scenario: Book a table
    Given I login as user "user" with password "password"
    When I book a table
      | people_number | date       | time_zone     |
      | 4             | 30/05/2022 | 12:30 - 14:00 |
    Then There is 1 booking