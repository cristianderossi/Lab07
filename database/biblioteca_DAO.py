from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca
from model.libro_DTO import Libro

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO

    def get_biblioteca(self) -> list[Libro]:

        cnx = DBConnect.get_connection()

        if cnx is None:
            raise ConnectionError('Errore')

        cursor = cnx.cursor(dictionary=True)
        try:

            query = """
               SELECT  id, nome , indirizzo 
               FROM  biblioteca b 
               order by nome

               """

            cursor.execute(query)

            result=[Biblioteca(**row) for row in cursor]
            return result


        finally:

            cursor.close()
            cnx.close()





