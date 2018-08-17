import unittest
import json
from users.views import app
from unittest import TestCase

class LoginTest(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.user_data = {
            "username":"kerenagemo",
            "password":"sasdfggjh"
        }