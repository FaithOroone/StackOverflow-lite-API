import unittest
import json
from users.views import app
from unittest import TestCase

class SignupTest(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.user_data = {
            "username":"kerenagemo",
            "password":"sasdfggjh"
        }

     def test_user_signup(self):
        response = self.app.post('api/v1/auth/login', data = json.dumps(self.user_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("you have successfully signed up", str(response.data))

    if __name__ == '__main__':
        unittest.main