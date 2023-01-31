import sqlite3
import json

load_json(data):
  conn = sqlite3.connect("database.db")
  cursor = conn.cursor()

  # Create a table for the data
  cursor.execute("""
  CREATE TABLE IF NOT EXISTS data (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      json_data TEXT
  )
  """)

  cursor.execute("INSERT INTO data (json_data) VALUES (?)", (json.dumps(data),))

  # Commit the changes and close the connection
  conn.commit()
  conn.close()
