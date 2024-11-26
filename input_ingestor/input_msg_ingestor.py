import json
from input_ingestor.AbstractReader import MainIngestor

#Reads messages from a file
class InputMsgIngestor(MainIngestor):

    def __init__(self, file_path):
        self.file_path = file_path

#Reads and returns messages from the file
    def read_msgs(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                yield json.loads(line)  # Convert each line to a dictionary
