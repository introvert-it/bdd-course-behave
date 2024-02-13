Feature: add todo item

  Scenario: add one todo item
    Given user opens todo app
    When user adds new todo item with text "Hello BDD"
    Then todo items list should contain 1 items
    And todo item with text "Hello BDD" should be present on the list

  Scenario: add multiple todo items
    Given user opens todo app
    When user adds 3 new todo items
    Then todo items list should contain 3 items
