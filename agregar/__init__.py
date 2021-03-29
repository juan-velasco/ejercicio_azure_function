import logging
import azure.functions as func
import mysql.connector
import os

DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')

    if name:
        cnx = mysql.connector.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=3306, database=DB_NAME)
        cursor = cnx.cursor()
        stmt = ("INSERT INTO `personas` (`id`, `nombre`) VALUES (NULL, %s)")
        cursor.execute(stmt, (name,))
        cnx.commit()

        return func.HttpResponse(f"Hola, {name}. Tu nombre ha sido agregado a la tabla.")
    else:
        return func.HttpResponse(
             "Debes indicar un nombre mediante un queryString, por ejemplo ?name=tyrion.",
             status_code=200
        )
