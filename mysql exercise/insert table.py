import mysql.connector

connection = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "2121",
    database = "hospital"
)
db = connection.cursor()
query = ("""INSERT INTO information(name, surname, Tc, Gender, Age, Location)
VALUES ("Masal","Elkıran","25489654785","Kadın",60,"Ardahan"),
("Cem","Gözağaç","25486587532","Erkek",42,"Isparta"),
("Veli","Dinçaslan","45856985475","Erkek",38,"Trabzon"), 
("Niyazi","Yeniçeri","89547854213","Erkek",23,"Diyarbakır")""")
db.execute(query)
connection.commit()