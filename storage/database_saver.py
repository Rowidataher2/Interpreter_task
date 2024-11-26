import sqlite3
from storage.AbstractStorage import BaseProducer


#output message producer phase
class DatabaseProducer(BaseProducer):
    def __init__(self, db_path):
        self.db_path = db_path

    def clear_table(self):
        """Clear the messages table for testing purposes."""
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        # delete all records
        cursor.execute("DELETE FROM messages")
        connection.commit()
        connection.close()

    def setup_database(self):
        """Ensure the database and table are properly initialized."""
        connection = sqlite3.connect(self.db_path)
        db_cur = connection.cursor()
        db_cur.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_id TEXT,
            attribute_id TEXT,
            timestamp TEXT,
            value TEXT
        )
        """)
        connection.commit()
        connection.close()



    def save_output(self, message, output):
        """Save processed messages to the database."""
        self.setup_database()  # Ensure the database is initialized
        connection = sqlite3.connect(self.db_path)
        #represents the cursor object in SQLite
        cursor_db = connection.cursor()
        cursor_db.execute("""
        INSERT INTO messages (asset_id, attribute_id, timestamp, value)
        VALUES (?, ?, ?, ?)
        """, (message["asset_id"], message["attribute_id"],
              message["timestamp"], str(output)))
        connection.commit()
        connection.close()



