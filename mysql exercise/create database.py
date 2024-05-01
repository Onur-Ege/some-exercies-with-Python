import mysql.connector

connection = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "2121"
)
db = connection.cursor()
query =("CREATE DATABASE hospital")
db.execute(query)