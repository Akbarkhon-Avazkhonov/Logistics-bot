import sqlite3

def create_category(category_name, category_message = "", category_interval=0):
    
    # Connect to database
    connect = sqlite3.connect('db.sqlite3')
    # Create a cursor
    db = connect.cursor()
    
    # Insert a row of data
    db.execute("INSERT INTO categories VALUES (NULL, ?, ?, ?)", (category_name, category_message, category_interval))

    # Save (commit) the changes
    connect.commit()

    # Close connection
    db.close()

def get_categories():
    categories = []
    # Connect to database
    connect = sqlite3.connect('db.sqlite3')
    # Create a cursor
    db = connect.cursor()
    # get all categories
    db.execute("SELECT category_name FROM categories")
    categories = db.fetchall()
    # Close connection
    db.close()
    return categories

def delete_category(category_name):
    # Connect to database
    connect = sqlite3.connect('db.sqlite3')
    # Create a cursor
    db = connect.cursor()
    
    # Insert a row of data
    db.execute("DELETE FROM categories WHERE category_name = ?", (category_name,))

    # Save (commit) the changes
    connect.commit()

    # Close connection
    db.close()


# async def send_messages(client, message):
#     for id in all_id:
#         try:
#             await client.send_message(id, message)
#         except Exception as e:
#             await client.send_message("me", "ERROR : " + str(e))
#             continue

