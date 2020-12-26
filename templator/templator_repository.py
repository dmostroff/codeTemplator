import pgsql_db_layer as db

def get_tables_by_prefix( prefix):
    sql = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME ~ %s"
    return db.fetchall(sql, prefix)