@fixture.setup.testing.db
Feature: List the menus
  Scenario: Display the existing menus
    When I ask for the list of menus
    Then I expect for a list that contains MagicMenu