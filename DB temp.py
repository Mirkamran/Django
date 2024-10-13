import sqlite3

# Step 1: Connect to the database
conn = sqlite3.connect('numbersapi.db')

# Step 2: Create a cursor object
cursor = conn.cursor()

# Step 3: Drop the table if it exists (this will delete all data and reset the ID counter)
cursor.execute("DROP TABLE IF EXISTS my_table;")

# Step 4: Recreate the table with the same structure
cursor.execute('''
    CREATE TABLE my_table (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Type TEXT NOT NULL,
        Value TEXT NOT NULL
    );
''')

# Step 5: Commit the changes to the database
conn.commit()

# Step 6: Close the connection
conn.close()
