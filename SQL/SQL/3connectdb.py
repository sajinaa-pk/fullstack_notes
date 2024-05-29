#Or you can try to access the database when making the connection:
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="PassSQL@123"
  database="yourdatabase name here'
)
#If the database does not exist, you will get an error.