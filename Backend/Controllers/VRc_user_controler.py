import bcrypt
from contextlib import contextmanager
from Backend.Connections.VRd_db_loader import DataBase

class AccessManager:
    def __init__(self):
        self.db = DataBase()

    @contextmanager
    def db_connection(self):
        conn = self.db.connect()
        try:
            yield conn
        finally:
            conn.close()

    def get_user(self, username: str) -> tuple:
        query = "SELECT * FROM user_data WHERE username = ?"
        with self.db_connection() as conn:
            user = self.db.fetch_one(query, (username,))
            return user if user else None

    def set_user(self, username: str, password: str, state: str, city: str):
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        query = "INSERT INTO user_data (username, password_hash, state, city) VALUES (?,?,?,?)"
        with self.db_connection() as conn:
            self.db.execute_query(query, (username, hashed_password, state, city))

    def manage_login(self, username: str, password: str) -> bool:
        user_details = self.get_user(username)
        if user_details and bcrypt.checkpw(password.encode(), user_details[2]):
            return True
        return False

    def manage_signup(self, username: str, password: str, state: str, city: str):
        if self.get_user(username):
            raise ValueError("User already exists")
        self.set_user(username, password, state, city)
        return True

    def manage_forgot_password(self, username: str, new_password: str):
        user_details = self.get_user(username)
        if user_details:
            if user_details[2] == bcrypt.hashpw(password.encode(), bcrypt.gensalt()):
                raise ValueError("New password cannot be the same as the old password")
            hashed_password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
            query = "UPDATE user_data SET password_hash = ? WHERE username = ?"
            with self.db_connection() as conn:
                self.db.execute_query(query, (hashed_password, username))
            return True
        return False

def main():
    am = AccessManager()
    if am.manage_login("test_user", "test_password"):
        print("Login successful")
    else:
        print("Login failed")
        try:
            am.manage_signup("test_user", "test_password", "test_state", "test_city")
            print("Signup successful")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
