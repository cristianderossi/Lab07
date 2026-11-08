
from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):

        pass
    # TODO


    def get_generi(self)->list[Biblioteca]:

        cnx=DBConnect.get_connection()

        if cnx is  None:
            raise ConnectionError('Errore')


        cursor=cnx.cursor()
        try:

            query= """
            Select distinct genere 
            from libro 
            where genere is not null 
            order by genere 
            """

            cursor.execute(query)

            result = [row[0] for row in cursor]
            return result

        finally:

         cursor.close()
         cnx.close()



    def get_libri_filtrati(self,genere,id_biblioteca):
        cnx=DBConnect.get_connection()
        if cnx is None:
            raise ConnectionError('Errore')


        cursor=cnx.cursor(dictionary=True)
        try:

            query= """
            Select *
            from libro 
            where genere = Coalesce(%s,genere) and  id_biblioteca =coalesce(%s,id_biblioteca)
             
             """

            cursor.execute(query,(genere,id_biblioteca))
            result=[Libro(**row) for row in cursor]
            return result


        finally:
            cursor.close()
            cnx.close()












            
                     
            






