import sqlite3

conn = sqlite3.connect('sqlite3Sample.db')
cursor = conn.cursor()

def create_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        email TEXT NOT NULL,
        password TEXT UNIQUE
    )
    """)
    conn.commit()

def Add_in_db():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    cursor.execute("""
    INSERT INTO users(name,age,email,password)
    VALUES(?,?,?,?)
    """,(name,age,email,password))
    conn.commit()
    print("Data Inserted")

def delete_data():
    id = int(input("Enter ID:"))
    cursor.execute("DELETE FROM users WHERE id = ?",(id,))
    conn.commit()
    print("Data Deleted")

def update_data():
    id = int(input("Enter ID:"))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    cursor.execute("""
    UPDATE users
    SET name=?, age=?, email=?, password=?
    WHERE id=?
    """,(name,age,email,password,id))
    conn.commit()
    print("Data Updated")

def read_data():
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    print()
    for row in data:
        print(row)

def search_data():
    name = input("Enter name to search: ")
    cursor.execute("SELECT * FROM users WHERE name = ?",(name,))
    row = cursor.fetchone()
    if row:
        print("Data Found:", row)
    else:
        print("Data Not Found")

def menu():
    create_db()  
    while True:
        print('''
    1. Add
    2. Read
    3. Update
    4. Delete
    5. Search
    (press anything else to Exit)''')
        
        
        choice = input("Enter Choice: ")
        if choice == "1":
            Add_in_db()
        elif choice == "2":
            read_data()
        elif choice == "3":
            update_data()
        elif choice == "4":
            delete_data()
        elif choice == "5":
            search_data()
        else:
            print("Exiting...")
            break

if __name__ == "__main__":
    menu()
    conn.close()
