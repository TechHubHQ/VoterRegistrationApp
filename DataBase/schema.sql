-- SQLite schema

-- User Data Table
CREATE TABLE IF NOT EXISTS user_data (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL UNIQUE,
  password_hash TEXT NOT NULL,
  state TEXT,
  city TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Index on username for faster lookups
CREATE INDEX IF NOT EXISTS idx_username ON user_data(username);

-- Trigger to update the updated_at timestamp
CREATE TRIGGER IF NOT EXISTS update_user_timestamp 
AFTER UPDATE ON user_data
BEGIN
  UPDATE user_data SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;