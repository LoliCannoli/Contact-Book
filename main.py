import sqlite3
from contactClass import Contact

database = sqlite3.connect(':memory:')
cursor = database.cursor()

cursor.execute("""CREATE TABLE contacts (
              firstName text,
              lastName text,
              phoneNumber integer,
              email text
              )""")

contact = Contact('Testing Name', 1234, 'email@email.com')
contact.insertToDatabase(database)

cursor.execute("SELECT * FROM contacts WHERE firstName = 'Testing'")
print(cursor.fetchall())

database.close()
