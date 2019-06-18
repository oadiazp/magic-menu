Feature: List the menus

  @fixture.setup_testing_db_and_add_default_menu
  Scenario: Display the existing menus
    When I ask for the list of menus
    Then I expect for a list that contains MagicMenu