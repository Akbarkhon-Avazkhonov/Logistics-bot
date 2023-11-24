import sqlite3

# Connect to database
conn = sqlite3.connect('db.sqlite3')
# Create a cursor
c = conn.cursor()

# create table

c.execute("""CREATE TABLE users (
            id integer,
            name text
            )""")

# Insert one record
c.execute("INSERT INTO users VALUES (123, 'John')")
# Insert many records at once
many_users = [
    (124, 'Jane'),
    (125, 'Bob'),
    (126, 'Peter'),
]
c.executemany("INSERT INTO users VALUES (?, ?)", many_users)

# Query the database
c.execute("SELECT * FROM users")
print(c.fetchall())


# Commit our command
conn.commit()

# Close our connection
conn.close()