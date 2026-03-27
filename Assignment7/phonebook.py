import csv
from connect import connect

def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(100) NOT NULL,
        phone VARCHAR(20) UNIQUE NOT NULL
    )
    """)

    conn.commit()
    cur.close()
    conn.close()

def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                cur.execute(
                    "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
                    (row[0], row[1])
                )
            except Exception as e:
                print("Error inserting:", row, e)

    conn.commit()
    cur.close()
    conn.close()

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
            (name, phone)
        )
        conn.commit()
        print("Inserted successfully!")
    except Exception as e:
        print("Error:", e)

    cur.close()
    conn.close()

def update_contact():
    choice = input("Update (1) Name or (2) Phone? ")

    conn = connect()
    cur = conn.cursor()

    if choice == '1':
        phone = input("Enter phone of contact: ")
        new_name = input("Enter new name: ")

        cur.execute(
            "UPDATE phonebook SET first_name = %s WHERE phone = %s",
            (new_name, phone)
        )

    elif choice == '2':
        name = input("Enter name of contact: ")
        new_phone = input("Enter new phone: ")

        cur.execute(
            "UPDATE phonebook SET phone = %s WHERE first_name = %s",
            (new_phone, name)
        )

    conn.commit()
    print("Updated!")

    cur.close()
    conn.close()

def query_contacts():
    print("1 - All contacts")
    print("2 - Search by name")
    print("3 - Search by phone prefix")

    choice = input("Choose: ")

    conn = connect()
    cur = conn.cursor()

    if choice == '1':
        cur.execute("SELECT * FROM phonebook")

    elif choice == '2':
        name = input("Enter name: ")
        cur.execute(
            "SELECT * FROM phonebook WHERE first_name ILIKE %s",
            ('%' + name + '%',)
        )

    elif choice == '3':
        prefix = input("Enter prefix: ")
        cur.execute(
            "SELECT * FROM phonebook WHERE phone LIKE %s",
            (prefix + '%',)
        )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

def delete_contact():
    print("Delete by: 1 - Name, 2 - Phone")
    choice = input("Choose: ")

    conn = connect()
    cur = conn.cursor()

    if choice == '1':
        name = input("Enter name: ")
        cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))

    elif choice == '2':
        phone = input("Enter phone: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))

    conn.commit()
    print("Deleted!")

    cur.close()
    conn.close()

def menu():
    while True:
        print("\n--- PHONEBOOK ---")
        print("1. Insert from CSV")
        print("2. Insert from console")
        print("3. Update contact")
        print("4. Query contacts")
        print("5. Delete contact")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == '1':
            insert_from_csv('contacts.csv')
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            query_contacts()
        elif choice == '5':
            delete_contact()
        elif choice == '0':
            break


if __name__ == "__main__":
    create_table()
    menu()