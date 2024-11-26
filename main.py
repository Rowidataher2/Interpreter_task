

import json
import time
import requests
from input_ingestor.input_msg_ingestor import InputMsgIngestor
from processing.processing_engine import ProcessingEngine
from storage.database_saver import DatabaseProducer


DB_PATH = "message_storage.db"
CONFIG_FILE = "configuration/equations.json"
API_URL = "http://127.0.0.1:8000/api/kpi/"
msgsFile= "messages.txt"

#get kpi equation,expretions from api
def get_equations():
    """Retrieve KPI equations from a remote API without using try-except."""
    response_api = requests.get(f"{API_URL}kpi/")

    # Check if the response was successful (HTTP Status code 200)
    if response_api.status_code == 200:
        return response_api.json()  # Return the JSON data if the status is OK
    else:
        print(f"Failed to retrieve KPI equations. HTTP status code: {response_api.status_code}")
        return []  # Return an empty list if request fails

def load_equations_from_file(file_path):
    """Load equations configuration from a JSON file."""
    with open(file_path, 'r') as config_file:
        return json.load(config_file)


def handle_message_processing(equations, ingestor, producer):
    """Processes messages, applies appropriate equations, and saves results."""
    for msg in ingestor.read_msgs():
        print(f"Processing message: {msg}")
        time.sleep(5)  #  get a msg every 5 seconds

        if isinstance(msg["value"], (int, float)):
            equation_to_apply = equations.get("arithmetic")  # For numeric values
        elif isinstance(msg["value"], str):
            equation_to_apply = equations.get("regex")  # For string values
        else:
            print(f"Unsupported value type: {type(msg['value'])}")
            continue

        if not equation_to_apply:
            print("No applicable equation found for this message.")
            continue

        # Apply the processing engine
        engine = ProcessingEngine(equation_to_apply)
        output = engine.process_message(msg)
        print(f"output: {output}")

        # Store the processed result in the database
        producer.save_output(msg, output)
        print("Message saved to the database.")


def main():
    # Load configuration equations from the JSON file
    equations = load_equations_from_file(CONFIG_FILE)

    if not equations:
        print("No equations available in the configuration.")
        exit(1)

    # Get messages from the file
    ingestor = InputMsgIngestor(msgsFile)

    # instance of the producer (to save results)
    producer = DatabaseProducer(DB_PATH)

    # Process and store the messages
    handle_message_processing(equations, ingestor, producer)


if __name__ == "__main__":
    main()
