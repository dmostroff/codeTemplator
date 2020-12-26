# mssql_db_layer
#
# DB Layer for MSSQL
#------------------------
import os
import sys
import psycopg2
from pandas import DataFrame
import pandas.io.sql as pdsql
import settings

def db_connector( func):
    def with_connection_(*args, **kwargs):
        conn = None
        connString = os.getenv('CONNECTION_STRING')
        if connString is None or connString == "":
            raise NameError("Connection string does not exist.")
        try:
            conn=psycopg2.connect( connString)
            return func( conn, *args, **kwargs)
        except Exception as e:
            print( sys.exc_info()[1])
            raise e
        finally:
            if conn:
                conn.close()
    return with_connection_
    

@db_connector
def get_sql_data_source_name( conn, arg=None, arg2=None):
    return conn.getinfo(pyodbc.SQL_DATA_SOURCE_NAME)

def get_server_name():
    return fetchone("SELECT inet_server_addr()")[0]

def get_database_name():
    return fetchone("SELECT current_database()")[0]

@db_connector
def get_version(conn, arg1=None, arg2=None):
    curs = conn.cursor()
    curs.execute( 'SELECT version();')
    return curs.fetchone()[0]

def does_table_exist(curs, table_name) -> bool:
    curs.execute( "SELECT COUNT(name) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = ?", [(table_name)])
    return curs.fetchone()[0] == 1

@db_connector
def create_table(conn, sql, table_name):
    curs = conn.cursor()
    curs.execute( sql)
    return does_table_exist(curs, table_name)

@db_connector
def read_sql_query(conn, sql, args=None):
    if args is None:
        df = pdsql.read_sql_query( sql, conn)
    else:
        sql_params = args if isinstance(args, list) else [args]
        df = pdsql.read_sql_query( sql, conn, params=sql_params)
    conn.commit()
    return df

@db_connector
def fetchall(conn, sql, args=None):
    if args is None:
        return pdsql.read_sql( sql, conn)
    sql_params = args if isinstance(args, list) else [args]
    try:
        return  pdsql.read_sql( sql, conn, params=sql_params)
    except Exception as ex:
        print( sys.exc_info()[1])
        raise ex

@db_connector
def fetchone(conn, sql, args=None):
    curs = conn.cursor()
    try:
        curs.execute( sql) if args is None else curs.execute(sql, args)
        res = curs.fetchone()
        conn.commit()
        return res
    except Exception as ex:
        print( sys.exc_info()[1])
        raise ex

@db_connector
def execute(conn, sql, args=None):
    try:
        curs = conn.cursor()
        if args is None:
            curs.execute( sql)
        else:
            curs.execute( sql, args)
        conn.commit()
    except Exception as ex:
        print( sys.exc_info()[1])
        raise ex

@db_connector
def does_exist(conn, sql, args=None):
    curs = conn.cursor()
    try:
        curs.execute( sql) if args is None else curs.execute(sql, args)
        return curs.fetchone()[0] == 1
    except Exception as ex:
        print( sys.exc_info()[1])
        raise ex
