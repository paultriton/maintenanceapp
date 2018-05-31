
"""tests_app.py"""
import unittest
import json
from app import APP

class FlaskTestCase(unittest.TestCase):
    """Test for app.py"""

    def test_get_request(self):
        """test get two request"""

        test_client = APP.test_client(self)

        response = test_client.put(
            '/api/v1/users/requests/93',
            data=json.dumps({"request":"hello"}), content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"modified request succesfully", response.data)


    def test_failed_get_request(self):
        """test not found to modify"""

        test_client = APP.test_client(self)

        response = test_client.put(
            '/api/v1/users/requests/93',
            data=json.dumps({"request":"hello"}), content_type="application/json"
        )

        self.assertIn(b"no request found", response.data)
