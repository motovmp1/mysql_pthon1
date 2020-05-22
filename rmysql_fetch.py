import mysql.connector
from mysql.connector import Error
import time

try:
    connection = mysql.connector.connect(host='127.0.0.1',
                                        port=3308,
                                         database='freecode_students',
                                         user='root',
                                         password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        database_selected = 'laptop'
        print(f'Table selected is --> {database_selected}')
        cursor.execute(f'select * from {database_selected};')
        out = cursor.fetchall()
        for nome in out:
            print(nome)
            time.sleep (0.2)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")