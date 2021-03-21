Feature: Draft
  Scenario: Save a shipment draft
    Given a registered client
    When a service has been selected
    Then it will save the shipment as a draft
    And it will appear in the shipment list
    Then close session