from ctypes.wintypes import CHAR, INT
from pyclbr import Function
from telnetlib import DO
from tkinter import END
import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Dhruv0808*",
    database="testdatabase"
)
print("WELCOME TO **AIRPLANE TRAFFIC MANAGEMENT SYSTEM**")
p_id=input("enter plane id:-")
a_time=float(input("enter arrival time:-"))
d_time=float(input("enter departure time:-"))
mycursor=db.cursor()
#mycursor.execute("CREATE TABLE airplane_schedule(plane_id VARCHAR(5) PRIMARY KEY, arrival_time FLOAT(4,2) , departure_time FLOAT(4,2) )")
#mycursor.execute("CREATE TABLE new_airplane_entries(plane_id VARCHAR(5) PRIMARY KEY, arrival_time FLOAT(4,2) , departure_time FLOAT(4,2) )")
#mycursor.execute("CREATE TABLE rejected_airplane_entries(plane_id VARCHAR(5) PRIMARY KEY, arrival_time FLOAT(4,2) , departure_time FLOAT(4,2) )")
mycursor.execute("INSERT INTO new_airplane_entries VALUES(%s,%s,%s)",(p_id,a_time,d_time) )
db.commit()
mycursor.execute("INSERT INTO rejected_airplane_entries SELECT %s,%s,%s from dual WHERE EXISTS (SELECT * FROM airplane_schedule WHERE ABS((FLOOR(%s)*60 + (%s-FLOOR(%s))*100.00)-(FLOOR(arrival_time)*60 + (arrival_time-FLOOR(arrival_time))*100.00))<5)",(p_id,a_time,d_time,a_time,a_time,a_time))
db.commit()
mycursor.execute("INSERT INTO airplane_schedule SELECT %s,%s,%s from dual WHERE NOT EXISTS (SELECT * FROM airplane_schedule WHERE ABS((FLOOR(%s)*60 + (%s-FLOOR(%s))*100.00)-(FLOOR(arrival_time)*60 + (arrival_time-FLOOR(arrival_time))*100.00))<5)",(p_id,a_time,d_time,a_time,a_time,a_time))
db.commit()
v=int(input("ENTER 1 to see updated airplane schedule...ENTER 2 to see rejected airplane entries...ENTER 3 to see all airplane entries:-"))
if(v==1):
    print("updated airplane schedule is as follows:-")
    mycursor.execute("SELECT * FROM airplane_schedule")
    for x in mycursor:
     print(x)  
elif(v==2):
    print("updated rejected_airplane_entries is as follows:-")
    mycursor.execute("SELECT * FROM rejected_airplane_entries")
    for y in mycursor:
        print(y)  
elif(v==3):
    print("all airplane entries is as follows:-")
    mycursor.execute("SELECT * FROM new_airplane_entries")
    for z in mycursor:
       print(z)  


