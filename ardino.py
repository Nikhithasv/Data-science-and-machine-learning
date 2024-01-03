import serial
import mysql.connector

def insert_data(mydata):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db"
        )
    my_arr = mydata.split(',')
    my=mydata.split(',')
    mycursor = mydb.cursor()
    sql='INSERT INTO colo(r,b,g,c) VALUES ('+my_arr[0]+','+my_arr[1]+','+my_arr[2]+','+my[0]+')'
    mycursor.execute(sql)
    mydb.commit()
    print("insertion success")

while True:
    myser = serial.Serial("COM5" ,9600,
                          parity=serial.PARITY_NONE,
                          stopbits=serial.STOPBITS_ONE,
                          bytesize=serial.EIGHTBITS)
    line  = (myser.readline())
    data = line.decode('utf-8')
    print(data)
    insert_data(data)
    myser.close()
