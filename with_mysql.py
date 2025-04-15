import mysql.connector

# Establish connection
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

cursor = conn.cursor()

# Execute query
cursor.execute("SELECT * FROM your_table")

# Fetch data
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close connection
cursor.close()
conn.close()

# Insert Data
query = "INSERT INTO users (name, age) VALUES (%s, %s)"
values = ("Aniket", 21)
cursor.execute(query, values)
conn.commit()


#update Data
query = "UPDATE users SET age = %s WHERE name = %s"
values = (22, "Aniket")
cursor.execute(query, values)
conn.commit()

# Delete Data
query = "DELETE FROM users WHERE name = %s"
cursor.execute(query, ("Aniket",))
conn.commit()

