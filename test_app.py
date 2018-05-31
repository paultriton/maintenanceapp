"""test_get.py"""
import unittest
from app import APP

class AppTests(unittest.TestCase):
    """Class for my tests"""
    def test_get_all(self):
        """Test get method"""
        tester = APP.test_client(self)
        response = tester.get('/api/v1/users/requests')
        self.assertEqual(response.status_code, 200)
