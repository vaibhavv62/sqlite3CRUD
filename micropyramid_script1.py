import sqlite3
con = sqlite3.connect('example.db')
cur = con.cursor()

create_table_query = "CREATE TABLE person (\
	name TEXT NOT NULL,\
	email TEXT NOT NULL UNIQUE,\
	phone TEXT NOT NULL UNIQUE,\
	age INT NOT NULL,\
	dob DATE NOT NULL\
        );"

while True:
    ch = input('\nDo you want to add a record(y/n)?')
    if ch == 'n' or ch == 'N':
        break
    n = input('Please enter your Name:')
    e = input('Please enter your Email ID:')
    p = input('Please enter your Phone No:')
    a = input('Please enter your age:')
    d = input('Please enter your Date of Birth:')

    insert_query = f"INSERT INTO person VALUES\
            ('{n}','{e}','{p}',{a},'{d}');"       

    try:
        cur.execute(insert_query)
        print('Person Record Inserted')

    except sqlite3.IntegrityError as ie:
        print('\n',ie,'\nA record with entered Email/Phone already exists,\nPlease Enter new email/phone')

con.commit()
con.close()

