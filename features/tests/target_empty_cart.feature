# Created by acryon at 4/3/24
Feature: target empty cart test

  Scenario: User verifies cart is empty
  Given Open Target main page
  When Click on cart icon
  Then Verify "Your cart is empty" message is shown

  Scenario: Logged out user can navigate to sign in
  Given Open Target main page
  When Verify sign in is clickable
  Then Verify sign in is clickable from right side navigation menu
  Then Verify "Sign into your Target account" message is shown
