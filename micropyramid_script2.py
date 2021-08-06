import sqlite3
con = sqlite3.connect('example.db')
cur = con.cursor()

while True:
    ch = input('\nDo you want to find a record(y/n)?')
    if ch == 'n' or ch == 'N':
        break
    n = input('Please enter Name to find out other details:')
    retrival_query = f"SELECT * FROM person WHERE name='{n}'"
    data = cur.execute(retrival_query)
    #print(data,type(data))
    data_found = False
    for row in data:
        data_found = True
        print(f'\nPerson Details:\n\nName:{row[0]}\nEmail:{row[1]}\nPhone No:{row[2]}\nAge:{row[3]}\nDate of Birth:{row[4]}')
    if not data_found:
        print(f'No Record Found with the name- {n}!')

con.close()
