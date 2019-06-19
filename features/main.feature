@fixture.setup_testing_db_and_add_default_menu
Feature: List the menus
  Scenario: Display the existing menus
    When I ask for the list of menus
    Then I expect for a list that contains MagicMenu

#  Scenario: Create a menu with submenus
#    When I add a submenu to a menu
#    Then The dict should contain a key called 'submenus'
#    And The submenu should have its options
