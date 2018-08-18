import unittest
import json
from users.views import app
from unittest import TestCase

class GetaQuestionTest(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.request_data = {
            "question_id":"question_id",
            "username":"username",
            "question":"question"
        }

    def test_get_a_question(self):
        response = self.app.get('/api/v1/question/<int:question_id>', data = json.dumps(self.request_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 302)
        self.assertIn("you have fetched one question", str(response.data))

    if __name__ == '__main__':
        unittest.main