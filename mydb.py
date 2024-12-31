import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'Your username',
    passwd = 'Your db passwd'
    )

cursor = database.cursor()

cursor.execute("CREATE DATABASE dcrmdb")

print("db created")
