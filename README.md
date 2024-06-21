# SQLite Python Programming Task

## Description
This coding task demonstrates basic operations with an SQLite database using Python. The script performs the following operations:
1. Creates a table named `python_programming`.
2. Inserts specified rows into the table.
3. Selects records with grades between 60 and 80.
4. Updates Carl Davis's grade.
5. Deletes Dennis Fredrickson's row.
6. Updates the grades of students with an ID greater than 55.
7. Verifies the changes by selecting all records.

This task is important for learning how to interact with databases using Python, which is a crucial skill for data management and application development.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Installation
To run this code locally, you need to have Python installed. You can download Python from [python.org](https://www.python.org/downloads/).

No additional libraries are required, as `sqlite3` is included in the Python Standard Library.

## Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/codingTasks.git
    cd codingTasks
    ```

2. Save the script as `sqlite_task.py`.

3. Run the script:
    ```bash
    python sqlite_task.py
    ```

4. You should see output that verifies the operations performed by the script:
    ```plaintext
    Records with grades between 60 and 80:
    (55, 'Carl Davis', 61)
    (77, 'Jane Richards', 78)

    All records after updates:
    (55, 'Carl Davis', 65)
    (77, 'Jane Richards', 80)
    (12, 'Peyton Sawyer', 45)
    (2, 'Lucas Brooke', 99)
    ```

## Credits
Author: Duri Kim
