import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="parkhi",port='3307')
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS new_schema")
mycursor.execute("USE new_schema")
mycursor.execute("CREATE TABLE IF NOT EXISTS register(fname VARCHAR(45), lname VARCHAR(45), contact varchar(10), email VARCHAR(45) primary key, secques VARCHAR(45), secqans VARCHAR(45), password VARCHAR(45))")
mydb.commit()
mycursor.execute("USE new_schema")
mycursor.execute("CREATE TABLE IF NOT EXISTS rants(email VARCHAR(45) REFERENCES register(email), rants TEXT(65535))")
mycursor.execute("INSERT INTO rants(emails) SELECT email FROM register where rants.email = register.email")
mydb.commit()
mycursor.close()