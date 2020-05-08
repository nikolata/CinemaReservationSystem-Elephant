import unittest
from admins_gateway import add_id_to_table
import sqlite3
from unittest.mock import patch


class TestAdminGateway(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect('test_admin.db')
        self.cursor = self.connection.cursor()
        CREATE_ADMINS = '''
            CREATE TABLE IF NOT EXISTS admins (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
            );
            '''
        self.cursor.execute(CREATE_ADMINS)


    def test_add_id_to_table(self, mock_query, mock_admin_query):
        pass


    def tearDown(self):
        destroy = '''
            DROP TABLE test_admins;
        '''
        self.cursor.execute(destroy)
        self.connection.close()

if __name__ == '__main__':
    unittest.main()
