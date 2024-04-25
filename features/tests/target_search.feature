# Created by acryon at 4/22/24
Feature: Item search test

  Scenario Outline: User can search for a product
    Given Open Target main page
    When Search for <item>
    Then Verify search results are shown for <expected_item>
    Examples:
    |item          |expected_item  |
    |soda          |soda           |
    |Cake mix      |Cake mix       |

  Scenario: Verify that every product has a name and an image
    Given Open target main page
    When Search for Nintendo Switch - OLED Model: Mario Red Edition
    Then Verify that every product has a name and an image