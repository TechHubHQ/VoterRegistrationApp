import os
import sqlite3


class DataBase:
    def __init__(self, db_name: str = "VRd_db.db", schema_file: str = "schema.sql"):
        self.db_name = db_name
        self.db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "DataBase", db_name)
        self.schema_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "DataBase")
        self.schema_file = os.path.join(self.schema_path, schema_file)
        self.conn = None
        self.cursor = None

    def connect(self):
        """Establish a database connection and create a cursor."""
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        return self.conn

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None

    def create_tables(self):
        """Create tables based on the SQL schema file, dropping existing ones first."""
        try:
            # Drop all existing user-defined tables
            # self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
            # tables = self.cursor.fetchall()
            # for table_name in tables:
            #     self.cursor.execute(f"DROP TABLE IF EXISTS {table_name[0]};")
            # self.conn.commit()

            # Execute schema script to create tables
            with open(self.schema_file, 'r') as sql_file:
                sql_script = sql_file.read()
            self.cursor.executescript(sql_script)
            self.conn.commit()
            print("Database schema executed successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred while creating tables: {e}")

    def initialize_database(self):
        """Initialize the database by connecting and creating tables."""
        self.connect()
        self.create_tables()

    def execute_query(self, query, params=None):
        """Execute a SQL query with optional parameters."""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred while executing query: {e}")

    def fetch_all(self, query, params=None):
        """Fetch all results from a SELECT query."""
        self.execute_query(query, params)
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        """Fetch one result from a SELECT query."""
        self.execute_query(query, params)
        return self.cursor.fetchone()


# Example usage
if __name__ == "__main__":
    db = DataBase()
    db.initialize_database()

    result = db.fetch_one("SELECT * FROM user_data WHERE username = ?", ("test_user",))

    if not result:
        # Example query
        db.execute_query("INSERT INTO user_data ( username, password_hash, state, city) VALUES (?, ?, ?, ?)",
                         ("test_user", "hashed_password", "test_state", "test_city",))

    print(result)

    db.close()
