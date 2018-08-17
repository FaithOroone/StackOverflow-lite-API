import unittest
import json
from users.views import app
from unittest import TestCase

class SignupTest(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.user_data = {
            "first_name":"keren",
            "last_name":"agemo",
            "username":"kerenagemo",
            "email":"keren@gmail",
            "password":"sasdfggjh",
            "confirm_password":"sasdfggjh"
        }