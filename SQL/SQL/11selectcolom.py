#We use the fetchall() method, which fetches all rows from the last executed statement.


#Selecting Columns

'''
To select only some of the columns in a table, use the "SELECT" statement followed by the column name(s):
'''
#Select only the name and address columns:

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="PassSQL@123",
  database="studentform"
 
)
mycursor = mydb.cursor()


mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
