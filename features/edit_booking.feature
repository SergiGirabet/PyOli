Feature: Edit Booking
  In order to edit the book of a table
  As a user
  I want to edit a book

  Background: There is a registered user, table and book
    Given Exists a user "user" with password "password"
    Given Exists a table "table" with capacity 4
    And I book a table
      | date                | people_number |
      | 2021-05-18 19:17:16 | 4             |

  Scenario: Edit the booking of a table
    Given I login as user "user" with password "password"
    #When I view the details for the "booking"
    When I edit the current "book"
      | date                |
      | 2021-05-20 20:20:20 |
    Then The new date of the booking is 2021-05-20 20:20:20
