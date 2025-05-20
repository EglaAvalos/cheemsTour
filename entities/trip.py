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
            cursor = connection.cursor(dictionary=True)
            cursor.execute(
                "SELECT id, name, city, country, latitude, longitude FROM trip"
            )
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
            cursor.execute(
                "INSERT INTO trip (name, city, country, latitude, longitude) VALUES (%s, %s, %s, %s, %s)",
                (trip.name, trip.city, trip.country, trip.latitude, trip.longitude),
            )
            connection.commit()
            return cursor.lastrowid
        except Error as ex:
            return str(ex)
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def update(cls, trip):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE trip SET name= %s, city= %s, country= %s,latitude= %s,longitude= %s WHERE id=%s",
                (trip.name, trip.city, trip.country, trip.latitude, trip.longitude),
            )
            connection.commit()
            return cursor.lastrowid
        except Error as ex:
            return str(ex)
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def delete(cls, id):
        """
        Deletes a trip from the database by ID

        Parameters:

         id(int): the ID of the trip to delete

        Returns:
         int: The number of rows affected (1 if successful, 0 if not found).
         str: Error message if the operation fails.
        """
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("DELET FROM trip WHERE id=%s", (id,))
            connection.commit()
            return cursor.rowcount
        except Error as ex:
            return str(ex)
        finally:
            cursor.close()
            connection.close()
