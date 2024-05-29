#Where

'''
Select With a Filter
When selecting records from a table, you can filter the selection by using the "WHERE" statement:

'''

#Select record(s) where the address is "Park Lane 38": result:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="PassSQL@123",
  database="studentform"
 
)
mycursor = mydb.cursor()


sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)