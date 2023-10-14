import unittest
from unittest.mock import patch, Mock

import hw4a

class TestHW4a(unittest.TestCase):

    @patch('builtins.input', return_value='sturner44444')
    @patch('hw4a.validID', return_value=True)
    def test_user(self, mock_validID, mock_input):
        self.assertEqual(hw4a.validID('sturner44444'), True)

    @patch('builtins.input', return_value='sturner44444')
    @patch('hw4a.getrepos', return_value=['SSW567', 1])
    def test_repos(self, mock_getrepos, mock_input):
        self.assertIn('SSW567', hw4a.getrepos('sturner44444'))
        self.assertNotIn('classifysquare', hw4a.getrepos('sturner44444'))
        self.assertIn(1, hw4a.getrepos('sturner44444'))
        self.assertNotIn(100, hw4a.getrepos('sturner44444'))      

if __name__=='__main__':
    unittest.main()
