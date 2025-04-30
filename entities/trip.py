from persistence.db import get_connection
from mysql.connector import Error

class Trip:

    def __init__(self, name, city, country):
        self.name = name
        self.city = city
        self.country = country

    @classmethod
    def get(cls):
        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary = True)
            cursor.execute('SELECT id, name, city, country FROM trip')
            return cursor.fetchall()
        except Error as ex:
            return str(ex)
        finally:
            cursor.close()
            connection.close()