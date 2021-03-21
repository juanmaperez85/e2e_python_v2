Feature: Register

    Scenario: Register a user
        Given an internet user
        When going to packlink_registro page
        Then it will see the registration form with required fields

    Scenario: Log in for a registered user
        Given an internet user
        When registered in packlink WITH credentials
        Then it will land into the platform dashboard
        Then close session
