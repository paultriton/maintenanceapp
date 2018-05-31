"""test_get.py"""
import unittest
from app import APP

class AppTests(unittest.TestCase):
    """Class for my tests"""
    def test_get_one(self):
        """Test get one method"""
        test_client = APP.test_client(self)
        response = test_client.get('/api/v1/users/requests/2')
        self.assertEqual(response.status_code, 200)

    def test_get_one_not_found(self):
        """Test get one method"""
        test_client = APP.test_client(self)
        response = test_client.get('/api/v1/users/requests/23')
        self.assertIn(b"no request found", response.data)
