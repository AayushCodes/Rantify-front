import mysql.connector

mydb = mysql.connector.connect(
  port="3307",
  host="localhost",
  user="root",
  password="parkhi"
)

print(mydb)
my_cursor = mydb.cursor()