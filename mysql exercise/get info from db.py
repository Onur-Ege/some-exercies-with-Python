import mysql.connector

connection = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "2121",
    database = "hospital"
)
db = connection.cursor()
db.execute("SELECT * FROM hospital.information")
query = db.fetchall()

for i in query:
    print(i)
