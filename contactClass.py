class Contact:
    def __init__(self, name, phone, email):
        name = name.split(' ')
        self.firstName = name[0]
        self.lastName = name[1]
        self.phone = phone
        self.email = email

    def insertToDatabase(self, database):
        cursor = database.cursor()

        cursor.execute("INSERT INTO contacts VALUES (?, ?, ?, ?)", (self.firstName, self.lastName, self.phone, self.email))

        database.commit()
