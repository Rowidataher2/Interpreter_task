# import unittest
# from input_ingestor.input_msg_ingestor import InputMsgIngestor
#
# class TestFileIngestor(unittest.TestCase):
#     def test_read_messages(self):
#         # Use the existing messages.txt file
#         ingestor = InputMsgIngestor("messages.txt")
#         messages = list(ingestor.read_messages())
#
#         # Adjust assertions based on messages.txt content
#         self.assertEqual(len(messages), 5)  # Assuming there are 4 messages
#         self.assertEqual(messages[0]["asset_id"], "123")  # Example assertion
#
#
#
#

import unittest
from input_ingestor.input_msg_ingestor import InputMsgIngestor

class MessageIngestionTest(unittest.TestCase):
    def test_message_loading(self):
        # Create an instance of the message ingestor using the file path
        file_reader = InputMsgIngestor("messages.txt")
        retrieved_messages = list(file_reader.read_msgs())

        # Validate the content of the loaded messages
        self.assertEqual(len(retrieved_messages), 5)  # Confirming there are 5 messages
        self.assertEqual(retrieved_messages[0]["asset_id"], "123")  # Check for asset_id in first message
        self.assertEqual(retrieved_messages[1]["attribute_id"], "456")  # Check for attribute_id in second message
