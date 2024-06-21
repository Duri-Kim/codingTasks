import sqlite3


try:
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    # Step1: Create the python_programming table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS python_programming (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            grade INTEGER NOT NULL
        )
    ''')

    # Step2: Insert the specified rows into the table
    students = [
        (55, 'Carl Davis', 61),
        (66, 'Dennis Fredrickson', 88),
        (77, 'Jane Richards', 78),
        (12, 'Peyton Sawyer', 45),
        (2, 'Lucas Brooke', 99)
    ]

    cursor.executemany(
        'INSERT INTO python_programming (id, name, grade) VALUES (?, ?, ?)',
        students
    )

    # Commit the changes
    conn.commit()

    # Step 3: Select all records with a grade between 60 and 80
    print("Records with grades between 60 and 80:")
    cursor.execute(
        'SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80'
    )
    for row in cursor.fetchall():
        print(row)

    # Step 4: Change Carl Davis's grade to 65
    cursor.execute(
        'UPDATE python_programming SET grade = 65 WHERE name = "Carl Davis"'
    )

    # Commit the change
    conn.commit()

    # Step 5: Delete Dennis Fredrickson's row
    cursor.execute(
        'DELETE FROM python_programming WHERE name = "Dennis Fredrickson"'
    )

    # Commit the change
    conn.commit()

    # Step 6: Change the grade of all students with an id 
    # greater than 55 to a grade of 80
    cursor.execute('UPDATE python_programming SET grade = 80 WHERE id > 55')

    # Commit the change
    conn.commit()

    # Step 7: Verify the changes by selecting all records
    print("\nAll records after updates:")
    cursor.execute('SELECT * FROM python_programming')
    for row in cursor.fetchall():
        print(row)


except Exception as e:
    print("An error occurred:", e)


finally:
    # Close the connection
    if conn:
        conn.close()
        print("SQLITE connection is closed")
