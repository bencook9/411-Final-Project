# Project created by: Ben Cook, Erik Konnath, James Coddington, Viet Ninh
# pip install mysql-connector, pip install wheel
import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "test"
)

cursor = connection.cursor()

query1 = "select * from test"

cursor.execute(query1)

table = cursor.fetchall()

for row in table:
    print(row)