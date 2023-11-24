from pyrogram import Client
# auth
from config import api_id, api_hash

app = Client("my_account", api_id=api_id, api_hash=api_hash)



#create db and tables
import sqlite3
# Connect to database
connect = sqlite3.connect('db.sqlite3')
# Create a cursor
db = connect.cursor()
# create tables
db.execute("""CREATE TABLE groups (
            id integer PRIMARY KEY AUTOINCREMENT,
            group_id integer,
            group_name text,
            category_id integer
            )""")
db.execute("""CREATE TABLE categories (
           id integer PRIMARY KEY AUTOINCREMENT,
           category_name text,
           category_message text,
           category_interval integer
              )""")


db.close()

app.run()

if __name__ == "__main__":
    pass