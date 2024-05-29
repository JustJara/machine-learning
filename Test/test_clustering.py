import unittest
from controller.clustering import process_csv_and_cluster
from controller.database import Database
from unittest.mock import MagicMock

class TestClustering(unittest.TestCase):
    def setUp(self):
        self.db = Database("postgresql://user:password@host/database")
        self.db.connect = MagicMock()
        self.db.create_tables = MagicMock()
        self.db.insert_clustering_result = MagicMock()

    def test_process_csv_and_cluster(self):
        success, message = process_csv_and_cluster(self.db, 'test.csv', 3)
        self.assertTrue(success)
        self.db.insert_clustering_result.assert_called_once()

if __name__ == '__main__':
    unittest.main()