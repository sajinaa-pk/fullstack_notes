#Drop Only if Exist
'''
If the the table you want to delete is already deleted, or for any other reason does not exist, you can use the IF EXISTS keyword to avoid getting an error.
'''
#Delete the table "customers" if it exists:

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="PassSQL@123",
  database="studentform"
 
)
mycursor = mydb.cursor()


sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)