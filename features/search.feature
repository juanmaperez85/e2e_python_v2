Feature: Search
  Scenario: Search services
    Given a registered client
    When create a order : "Madrid" "Madrid" "1" kg "10"cm x "10" cm x "10" cm
    Then it will select the first service of the list
    Then close session