import sqlite3

# Function to connect to the database
def connect(fileType, fileName):
    return sqlite3.connect(fileName + "." + fileType)

# Connect to the database
conn = connect("db", "database")

# Create a cursor to execute queries
cursor = conn.cursor()

# Create a table
cursor.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT, file_type TEXT)")

# Function to add an item
def add_item(name, file_type):
    cursor.execute("INSERT INTO items (name, file_type) VALUES (?, ?)", (name, file_type))
    conn.commit()

# Function to delete an item
def delete_item(id):
    cursor.execute("DELETE FROM items WHERE id = ?", (id,))
    conn.commit()

def update_item(id, name, file_type):
    cursor.execute("UPDATE items SET name = ?, file_type = ? WHERE id = ?", (name, file_type, id))
    conn.commit()


# Function to search for an item
def search_item(name):
    cursor.execute("SELECT * FROM items WHERE name LIKE ?", (name,))
    return cursor.fetchall()

def delete_all_items():
    cursor.execute("DELETE FROM items")
    conn.commit()

delete_all_items()
# Add some items
add_item("apple", "txt")
add_item("banana", "jpg") 
add_item("orange", "png")

# Search for items
print(search_item("apple"))  # Should print [(1, "apple", "txt"), (2, "banana", "jpg"), (3, "orange", "png")]

# Delete an item
delete_item(2)

# Search for items again
print(search_item("banana"))  # Should print [(1, "apple", "txt"), (3, "orange", "png")]
