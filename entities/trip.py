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
        """
    Actualiza un viaje en la base de datos.

    Parámetros:
    - trip (Trip): Objeto Trip con los datos actualizados, incluyendo el ID.

    Retorna:
    - int: Número de filas afectadas (1 si se actualizó correctamente, 0 si no se encontró el ID).
    - str: Mensaje de error si ocurre un problema con la base de datos.

    Ejemplo de uso:
        trip = Trip(id=3, name="Viaje a Cusco", city="Cusco", country="Perú", latitude=-13.5319, longitude=-71.9675)
        resultado = Trip.update(trip)
    """
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute('UPDATE trip SET name= %s, city= %s, country= %s,latitude= %s,longitude= %s WHERE id=%s',
                           (trip.name, trip.city, trip.country, trip.latitude, trip.longitude, trip.id))
            connection.commit()
            return cursor.rowcount
        except Error as ex:
            return str(ex)
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def delete(cls, id):
        """
    Elimina un viaje de la base de datos según su ID.

    Parámetros:
    - id (int): ID del viaje a eliminar.

    Retorna:
    - int: Número de filas afectadas (1 si se eliminó correctamente, 0 si no se encontró el ID o hubo un error).

    Ejemplo de uso:
        filas_afectadas = Trip.delete(3)

    Nota:
    - Si ocurre un error durante la conexión o ejecución, se imprime el mensaje y se retorna 0.
    """
        connection = None
        cursor = None
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM trip WHERE id=%s", (id,))
            connection.commit()
            return cursor.rowcount
        except Error as ex:
            return 0
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

