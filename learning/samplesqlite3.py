# import sqlite3

# # Connect to database
# conn = sqlite3.connect("mydata.db")
# cur = conn.cursor()

# # Create table
# cur.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER)")

# # Insert data
# cur.execute("INSERT INTO users VALUES (?, ?)", ("Jay", 22))

# # Read data
# cur.execute("SELECT * FROM users")
# print(cur.fetchall())

# # Save & close
# conn.commit()
# conn.close()


# import sqlite3

# # 1. Connect to database (creates file if not exists)
# conn = sqlite3.connect("mydata.db")
# cursor = conn.cursor()

# # 2. Create table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     age INTEGER
# )
# """)

# # 3. Insert data
# cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Jay", 22))
# cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Veer", 25))

# # 4. Read data
# print("\n--- All Users ---")
# cursor.execute("SELECT * FROM users")
# for row in cursor.fetchall():
#     print(row)

# # 5. Update data
# cursor.execute("UPDATE users SET age = ? WHERE name = ?", (23, "Jay"))

# # 6. Read updated data
# print("\n--- After Update ---")
# cursor.execute("SELECT * FROM users")
# for row in cursor.fetchall():
#     print(row)

# # 7. Delete data
# cursor.execute("DELETE FROM users WHERE name = ?", ("Veer",))

# # 8. Read after delete
# print("\n--- After Delete ---")
# cursor.execute("SELECT * FROM users")
# for row in cursor.fetchall():
#     print(row)

# # 9. Save and close
# conn.commit()
# conn.close()

import sqlite3

conn = sqlite3.connect("mydata.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name Text , age INTEGER)")
cursor.execute("Insert into users(name,age) values(?,?)",('jay',19))
cursor.execute("Insert into users(name,age) values(?,?)",('veer',22))

records = [('malay',24),('amit',30)]

cursor.executemany("Insert into users(name,age) values(?,?)",records)

cursor.execute("select * from users")
print("Fetch One:",cursor.fetchone())


conn.commit()
conn.close()