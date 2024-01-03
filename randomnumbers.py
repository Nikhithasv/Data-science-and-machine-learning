import random
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="",database="db")

myser = mydb.cursor()
sq="create table tew(Rvalue INT)"
myser.execute(sq)
def my_function(value):
  print("table created")
  sql = "INSERT INTO tew(Rvalue) VALUES("+str(random_number)+")" 
  myser.execute(sql)
  mydb.commit()
while True:
    random_number = random.randint(100,500)
    print("Random number:", random_number)
   
    my_function(random_number)
