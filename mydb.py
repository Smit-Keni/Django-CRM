import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Smit@2003'
    )

cursor = database.cursor()

cursor.execute("CREATE DATABASE dcrmdb")

print("db created")