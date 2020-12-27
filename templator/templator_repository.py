import pgsql_db_layer as db

def get_tables_by_prefix( schema, prefix):
    sql = """
SELECT TABLE_NAME
FROM INFORMATION_SCHEMA."tables"
WHERE table_schema = %s AND table_type = 'BASE TABLE'
    AND TABLE_NAME ~ %s
"""
    return db.fetchall(sql, [schema, prefix])

def get_column_info( schema, table_name):
    sql = """
SELECT ORDINAL_POSITION, COLUMN_NAME, DATA_TYPE, udt_name
FROM INFORMATION_SCHEMA.COLUMNS
WHERE table_schema = %s AND TABLE_NAME = %s
"""
    return db.fetchall(sql, [schema, table_name])
