import sqlite3
import function

# Establish database connection
db_connection = sqlite3.connect("sqlite.db")
print(db_connection)

# Create a cursor object
db_cursor = db_connection.cursor()
print(db_cursor)

# Execute a SELECT query
query1 = "SELECT * FROM demo"
db_cursor.execute(query1)

# Fetch and print one row
print("Reading 1 row")
row = db_cursor.fetchone()
print(row)

# Fetch and print three rows
print("Reading 3 rows")
rows = db_cursor.fetchmany(3)
for r in rows:
    print(r)

# Fetch and print all remaining rows
print("Reading all rows")
rows = db_cursor.fetchall()
for r in rows:
    print(r)

# Insert a new record into the 'demo' table
query2 = "INSERT INTO demo (Name, Hint) VALUES ('Michael', 'Murphy')"
db_cursor.execute(query2)
db_connection.commit()

# Query responder function for fetch operations
function.query_responder(db_cursor, "fetchmany", 3)
function.query_responder(db_cursor, "fetchall")

# User input for filtering results
id = int(input("Enter an ID: "))
query3 = "SELECT * FROM demo WHERE ID > ?"
# db_cursor.execute(query3, (id,))

# Call query responder function to fetch results
# function.query_responder(db_cursor, "fetchall")


