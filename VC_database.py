import sqlite3

# Connect to an in-memory SQLite database (replace ':memory:' with a file path if needed)
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Read and execute each SQL statement in the script
# Read and execute each SQL statement in the script
script_path = 'Breachforums.vc Database.sql'
with open(script_path, 'r') as script_file:
    for statement in script_file.read().split(';'):
        print(f"Executing: {statement.strip()}")
        try:
            cursor.execute(statement)
        except sqlite3.Error as e:
            print(f"Error executing statement: {e}")


# Perform a query and fetch data (replace 'your_table_name' with the actual table name)
query = 'SELECT * FROM mybb_users'
cursor.execute(query)
rows = cursor.fetchall()

# Display the data
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
