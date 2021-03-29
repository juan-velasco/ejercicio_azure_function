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

    cnx = mysql.connector.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=3306, database=DB_NAME)
    cursor = cnx.cursor()
    cursor.execute("SELECT nombre FROM `personas`")
    results = cursor.fetchall()

    resp = ""

    for row in results:
        resp += '\n >> ' + str(row[0])

    return func.HttpResponse(f"Personas:{resp}")
