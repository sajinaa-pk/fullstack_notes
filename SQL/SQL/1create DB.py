import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="PassSQL@123"
)

mycursor = mydb.cursor()

#create a data base
mycursor.execute("CREATE DATABASE studentform")




