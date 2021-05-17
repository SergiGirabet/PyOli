Feature: Edit Booking
  In order to edit the book of a table
  As a user
  I want to edit a book

  Background: There is a registered user, table and book
    #Given Exists a user "user" with password "password"
    #Given Exists a table "table" with capacity 2
    Given Exists a book by "user" with password "password" at the table "table" 2 people this "date" day

  Scenario: Book a table
    Given I login as user "user" with password "password"
    When I edit a book
      | people_number | date
      | 1             | 2021-05-18 20:17:16 |
    Then The new date of the booking is 2021-05-18 20:17:16