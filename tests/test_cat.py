import unittest
from unittest.mock import patch, Mock

from lib.cat import Cat

class TestCatMethods(unittest.TestCase):

    def setUp(self):
        self.mock_db_patch = patch('lib.cat.Database')
        self.mock_db = self.mock_db_patch.start()
        self.addCleanup(self.mock_db_patch.stop)
        self.cat_instance = Cat()

    def test_get_cats(self):
        mock_session = Mock()
        self.mock_db.return_value.driver.session.return_value.__enter__.return_value = mock_session
        mock_session.execute_write.return_value = [{"id": 1, "name": "Fluffy", "status": "Healthy"}]

        with self.subTest("Test get_cats method"):
            result = self.cat_instance.get_cats()
            self.assertEqual(result, [{"id": 1, "name": "Fluffy", "status": "Healthy"}])

    def test_get_cat(self):
        mock_session = Mock()
        self.mock_db.return_value.driver.session.return_value.__enter__.return_value = mock_session
        mock_session.read_transaction.return_value = {"id": 1, "name": "Whiskers", "status": "Adopted"}

        with self.subTest("Test get_cat method"):
            result = self.cat_instance.get_cat(cat_id=1)

            self.assertEqual(result, {"id": 1, "name": "Whiskers", "status": "Adopted"})

if __name__ == '__main__':
    unittest.main()
