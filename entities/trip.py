from persistence.db import get_connection
from mysql.connector import Error

class Trip:

    def __init__(self, name, city, country, latitude, longitude):
        self.name = name
        self.city = city
        self.country = country
        self.latitude = latitude
        self.longitude = longitude

    @classmethod
    def get(cls):
        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary = True)
            cursor.execute('SELECT id, name, city, country, latitude, longitude FROM trip')
            return cursor.fetchall()
        except Error as ex:
            return str(ex)
        finally:
            cursor.close()
            connection.close()
    
    @classmethod
    def save(cls, trip):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute('INSERT INTO trip (name, city, country, latitude, longitude) VALUES (%s, %s, %s, %s, %s)',
                           (trip.name, trip.city, trip.country, trip.latitude, trip.longitude))
            connection.commit()
            return cursor.lastrowid
        except Error as ex:
            return str(ex)
        finally:
            cursor.close()
            connection.close()