import psycopg2
import os

def guardar(datos):
 local_cursor = get_cursor()
 set_word(local_cursor, datos)
 close_cursor(local_cursor)

def get_cursor():
 conn = psycopg2.connect(database=os.environ['OPENSHIFT_APP_NAME'],
           	user=os.environ['OPENSHIFT_POSTGRESQL_DB_USERNAME'],
           	password=os.environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD'],
           	host=os.environ['OPENSHIFT_POSTGRESQL_DB_HOST'],
           	port=os.environ['OPENSHIFT_POSTGRESQL_DB_PORT'] )
 cursor = conn.cursor()
 return cursor

def close_cursor(cursor):
 conn = cursor.connection
 cursor.close()
 conn.close()

def mostrar():
 cursor = get_cursor()
 sql = "select data from datos;"
 cursor.execute(sql)
 result = [""+item[0]+"<P>" for item in cursor.fetchall()]
 close_cursor(cursor)
 return str(result)


def set_word(cursor, data):
 sql = "BEGIN;insert into datos (data) values ('"+data+"');COMMIT;"
 cursor.execute(sql)
 close_cursor(cursor)


