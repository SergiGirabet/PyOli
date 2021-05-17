Feature: Add Booking
  In order to book a table
  As a user
  I want to add a book

  Background: There is a registered user and table
    Given Exists a user "user" with password "password"
    Given Exists a table "table" with capacity 4


  Scenario: Book a table
    Given I login as user "user" with password "password"
    When I book a table
      | date                | people_number |
      | 2021-05-18 19:17:16 | 4             |
    Then There is 1 booking