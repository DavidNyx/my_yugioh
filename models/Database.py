import mysql.connector
from dotenv import load_dotenv
import os
import time

class MySQLDatabase:
    def __init__(self, host, user, database):
        self.host = host
        self.user = user
        self.database = database
        self.connection = None

    def connect(self, counter=0):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                database=self.database
            )
        except mysql.connector.Error as e:
            print("Error connecting to MySQL database:", e)
            time.sleep(5)
            c = counter + 1
            if c < 6:
                print("Try again atempt: ", str(c))
                self.connect(counter=c)
            else:
                print("Failed to connect to MySQL database after 5 attempts.")

    def disconnect(self):
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()

    def execute_query(self, query, order=None, order_by=None, limit=0):
        try:
            if order is not None and order_by is not None:
                query = query + f' ORDER BY `{order}` {order_by}'
            if limit > 0:
                query = query + f' LIMIT {limit}'
            try:
                print('query: ', query)
            except:
                print("utf-8 query: ", query.encode('utf-8'))
            cursor = self.connection.cursor()
            cursor.execute(query)
            
            if limit == -1:
                result = cursor.lastrowid
                cursor.fetchall()
            elif limit == 0 or limit > 1:
                result = cursor.fetchall()
            elif limit == 1:
                result = cursor.fetchone()
            else:
                result = None
                
            cursor.close()
            self.connection.commit()
            return result
        except mysql.connector.Error as e:
            print("Error executing query:", e)
            return None

load_dotenv()
DB = MySQLDatabase(host=os.getenv("DB_HOST"), user=os.getenv("DB_USER"), database=os.getenv("DB_NAME"))