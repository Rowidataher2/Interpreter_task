
import unittest
from input_ingestor.input_msg_ingestor import InputMsgIngestor
from processing.processing_engine import ProcessingEngine
from storage.database_saver import DatabaseProducer
import sqlite3

class Test_msgProcessor(unittest.TestCase):
    def setUp(self):
        """Set up the test environment by clearing the database"""
        self.producer = DatabaseProducer("message_processor.db")
        self.producer.clear_table()  # Clear the database before each test
        self.ingestor = InputMsgIngestor("messages.txt")

    def test_functionality(self):
        # Process all messages and save to the database
        for message in self.ingestor.read_msgs():
            if isinstance(message["value"], (int, float)):
                equation = "ATTR + 50 * (ATTR / 10)"
            elif isinstance(message["value"], str):
                equation = "Regex(ATTR, '^dog')"
            else:
                equation = None

            if equation:
                engine = ProcessingEngine(equation)
                processed_value = engine.process_message(message)
                self.producer.save_output(message, processed_value)

        # Verify data in the database
        connection = sqlite3.connect("message_processor.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM messages")
        rows = cursor.fetchall()
        self.assertGreater(len(rows), 0)
        connection.close()