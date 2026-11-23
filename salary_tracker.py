import sqlite3

with sqlite3.connect('salary_tracker.db') as conn:

    try:
        conn.execute('DELETE FROM salary_tracker')
    except:
        print('Attempted to clear the table if it existed ...')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS salary_tracker (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            salary REAL NOT NULL)''')

    arr =[]
    arr.append(['frank','technology',500])
    arr.append(['john','technology',5000])

    try:

        conn.executemany('''
            INSERT INTO salary_tracker(name,department,salary)
            VALUES (?,?,?)
            ''',arr)
        cursor = conn.execute('SELECT * FROM salary_tracker')

        print('All rows initially created in a SQL database: ')

        for x in cursor.fetchall(): print(x)

        print('\n')

    except sqlite3.IntegrityError:
        print('error')

    try:
        conn.execute('''DELETE FROM salary_tracker 
                        WHERE salary < ?''',(5000,))
    except:
        print('error2')

    try:

        conn.execute('''DELETE FROM salary_tracker WHERE id NOT IN (SELECT MIN(id) FROM salary_tracker_and_dog GROUP BY name, department, salary)''')
        cursor = conn.execute('SELECT * FROM salary_tracker WHERE salary > ?',
                            (501,))

        rows = cursor.fetchall()
        print('All rows after deletion: ')
        for x in rows: print(x)
        print('\n')
    except:
        print('error3')

    try:
        arr = []
        arr.append(['josie','technology',700])
        arr.append(['rebecca','technology',6000])
        arr.append(['luna','technology',20000])
        conn.executemany('''
                         INSERT INTO salary_tracker(name, department, salary)
                         VALUES (?, ?, ?)
                         ''', arr)
        cursor = conn.execute('SELECT * FROM salary_tracker')
        print('All rows after insertion: ')
        for x in cursor.fetchall(): print(x)

        print('\n')
    except:
        print('error adding rows')
    try:
        cursor = conn.execute('''SELECT * FROM salary_tracker ''')
        print('Fetched all rows: ')
        for x in cursor.fetchall(): print(x)
        print('\n')

    except:
        print('error select all')
    try:

        conn.executemany('UPDATE salary_tracker SET salary = ? WHERE name = ?',
                     [(950,'john'),(7000,'luna')],)
        rows = conn.execute('''SELECT * FROM salary_tracker WHERE salary IN (?,?)''',
                            (7000,950),)
        print('Updated rows: ')
        for x in rows: print(x)
    except:
        print('Update error')

    try:
        cursor = conn.execute('''SELECT COUNT(*) FROM salary_tracker''')
        print(cursor.fetchall())

    except:
        print('Count all error')


    print('\nFinal row(s)')
    conn.execute('''DELETE
                    FROM salary_tracker
                    WHERE id NOT IN (SELECT MIN(id) FROM salary_tracker GROUP BY name, department, salary)''')
    cursor = conn.execute('SELECT * FROM salary_tracker WHERE salary > ?',
                          (501,))

    rows = cursor.fetchall()
    for x in rows: print(x)



