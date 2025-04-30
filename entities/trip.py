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
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT id, name, city, country FROM trip')
            return cursor.fetchall()
        except Error as ex:
            return {'error': str(ex)}
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def get_by_id(cls, trip_id):
        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT id, name, city, country FROM trip WHERE id = %s', (trip_id,))
            result = cursor.fetchone()
            return result if result else {'message': 'Trip not found'}
        except Error as ex:
            return {'error': str(ex)}
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def create(cls, name, city, country):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute('INSERT INTO trip (name, city, country) VALUES (%s, %s, %s)', (name, city, country))
            connection.commit()
            return {'message': 'Trip created successfully'}
        except Error as ex:
            return {'error': str(ex)}
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def update(cls, trip_id, name, city, country):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute('UPDATE trip SET name = %s, city = %s, country = %s WHERE id = %s', (name, city, country, trip_id))
            connection.commit()
            if cursor.rowcount > 0:
                return {'message': 'Trip updated successfully'}
            else:
                return {'message': 'Trip not found'}
        except Error as ex:
            return {'error': str(ex)}
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def delete(cls, trip_id):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute('DELETE FROM trip WHERE id = %s', (trip_id,))
            connection.commit()
            if cursor.rowcount > 0:
                return {'message': 'viaje elimnado'}
            else:
                return {'message': 'viaje no encontrado'}
        except Error as ex:
            return {'error': str(ex)}
        finally:
            cursor.close()
            connection.close()
