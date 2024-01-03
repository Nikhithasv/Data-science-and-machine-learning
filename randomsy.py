import random
import mysql.connector

# Establish a connection to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db"
)

# Create a cursor object to execute SQL queri
