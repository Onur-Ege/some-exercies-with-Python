import mysql.connector

connection = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "2121",
    database = "hospital"
)
db = connection.cursor()
query =("CREATE TABLE information(id INT(5) UNSIGNED AUTO_INCREMENT PRIMARY KEY, name VARCHAR(25) NOT NULL, surname VARCHAR(25) NOT NULL, Tc VARCHAR(11) NOT NULL,Gender VARCHAR(5) NOT NULL,Age INT(2) NOT NULL,Location VARCHAR(20) NOT NULL)")
db.execute(query)