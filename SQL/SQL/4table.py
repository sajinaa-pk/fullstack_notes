#Creating a Table
'''
To create a table in MySQL, use the "CREATE TABLE" statement.

Make sure you define the name of the database when you create the connection

'''

#Create a table named "customers":

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="PassSQL@123",
  database="studentform"
 
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")