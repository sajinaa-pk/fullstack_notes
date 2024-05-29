#Drop Table
'''
Delete a Table
You can delete an existing table by using the "DROP TABLE" statement:

'''

#Delete the table "customers":

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="PassSQL@123",
  database="studentform"
 
)
mycursor = mydb.cursor()


sql = "DROP TABLE customers"

mycursor.execute(sql)