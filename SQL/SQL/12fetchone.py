#Using the fetchone() Method

'''
If you are only interested in one row, you can use the fetchone() method.

The fetchone() method will return the first row of the result:

'''
#Fetch only one row:

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="PassSQL@123",
  database="studentform"
 
)
mycursor = mydb.cursor()



mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)




