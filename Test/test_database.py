import unittest
import sys
sys.path.append('src')
from unittest.mock import MagicMock, patch
from controller.database import Database

class TestDatabase(unittest.TestCase):
    @patch('psycopg2.connect')
    def setUp(self, mock_connect):
        self.mock_conn = MagicMock()
        self.mock_cursor = MagicMock()
        mock_connect.return_value = self.mock_conn
        self.mock_conn.cursor.return_value = self.mock_cursor

        self.db = Database("postgresql://user:password@host/database")
        self.db.connect()

    def test_create_tables(self):
        self.db.create_tables()
        self.mock_cursor.execute.assert_called_once()

    def test_insert_clustering_result(self):
        self.db.insert_clustering_result('test.csv', 3, [0, 1, 2])
        self.mock_cursor.execute.assert_called_once()
        self.mock_conn.commit.assert_called_once()

    def tearDown(self):
        self.db.close()

if __name__ == '__main__':
    unittest.main()
