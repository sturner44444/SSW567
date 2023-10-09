import unittest
import hw4a

class TestHW4a(unittest.TestCase):

    def test_user(self):
        self.assertEqual(hw4a.validID('sturner44444'), True)

    def test_repos(self):
        self.assertIn('SSW567', hw4a.getrepos('sturner44444'))
        self.assertNotIn('classifysquare', hw4a.getrepos('sturner44444'))
        self.assertIn(13, hw4a.getrepos('sturner44444'))
        self.assertNotIn(15, hw4a.getrepos('sturner44444'))      

if __name__=='__main__':
    unittest.main()
