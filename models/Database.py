import mysql.connector
from dotenv import load_dotenv
import os

class MySQLDatabase:
    def __init__(self, host, user, database):
        self.host = host
        self.user = user
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                database=self.database
            )
        except mysql.connector.Error as e:
            print("Error connecting to MySQL database:", e)

    def disconnect(self):
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            
            if query.find('INSERT') != -1:
                result = cursor.lastrowid
            else:
                result = cursor.fetchall()
                
            cursor.close()
            self.connection.commit()
            return result
        except mysql.connector.Error as e:
            print("Error executing query:", e)
            return False

load_dotenv()
DB = MySQLDatabase(host=os.getenv("DB_HOST"), user=os.getenv("DB_USER"), database=os.getenv("DB_NAME"))