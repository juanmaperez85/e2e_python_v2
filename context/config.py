import os
import json

settings = None


class Settings(object):
    """Simple singleton class for managing and accessing settings"""
    def __init__(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testsettings.json')) as f:
            settings = json.load(f)
            self.login_url = settings['login-url']
            self.logout_url = settings['logout-url']
            self.user = settings['user']
            self.password = settings['password']
            self.register_url = settings['register-url']
            self.shipment_url = settings['shipment-url']
            self.create_url = settings['create-url']
            self.draft_url = settings['draft-url']
            self.browser = settings['browser']
            self.driver_timeout = int(settings['driver_timeout'])


settings = Settings()
