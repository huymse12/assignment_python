import mysql.connector


def connect_my_sql():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345678',
        database="LAPTOP"
    )
    return mydb
