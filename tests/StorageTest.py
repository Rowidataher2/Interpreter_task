# import unittest
# import sqlite3
# from storage.database_saver import DatabaseProducer
#
# class TestDatabaseProducer(unittest.TestCase):
#     def setUp(self):
#         """Clear the database before each test"""
#         self.producer = DatabaseProducer("message_processor.db")
#         self.producer.clear_table()  # Clear the database
#         self.message = {"asset_id": "123", "attribute_id": "A1", "timestamp": "2024-11-19T10:00:00Z", "value": 100}
#
#     def test_save_to_database(self):
#         processed_value = 600.0
#         self.producer.save_output(self.message, processed_value)
#
#         # Check if the message is saved in the database
#         connection = sqlite3.connect("message_processor.db")
#         cursor = connection.cursor()
#         cursor.execute("SELECT * FROM messages WHERE asset_id=?", (self.message["asset_id"],))
#         row = cursor.fetchone()
#         self.assertIsNotNone(row)  # Ensure the row is saved
#         self.assertEqual(row[1], self.message["asset_id"])  # Check asset_id
#         self.assertEqual(row[4], str(processed_value))  # Check processed value
#         connection.close()


import unittest
import sqlite3
from storage.database_saver import DatabaseProducer

class DatabaseSaverTests(unittest.TestCase):
    def setUp(self):
        """Setup method to initialize database and prepare test message."""
        self.db_path = "message_processor.db"
        self.saver = DatabaseProducer(self.db_path)
        self.saver.clear_table()  # Clear the database before each test
        self.test_message = {
            "asset_id": "123",
            "attribute_id": "A1",
            "timestamp": "2024-11-19T10:00:00Z",
            "value": 100
        }

    def test_inserting_processed_data(self):
        """Test the insertion of processed message into the database."""
        calculated_value = 60
        self.saver.save_output(self.test_message, calculated_value)

        # Verify that the message has been inserted correctly
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM messages WHERE asset_id=?", (self.test_message["asset_id"],))
        fetched_row = cursor.fetchone()
        self.assertIsNotNone(fetched_row, "The record should exist in the database.")  # Ensure data was saved
        self.assertEqual(fetched_row[1], self.test_message["asset_id"], "Asset ID should match.")
        self.assertEqual(fetched_row[4], str(calculated_value), "Processed value should match the saved value.")
        connection.close()
