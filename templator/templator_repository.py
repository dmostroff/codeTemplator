import pgsql_db_layer as db

def create_routes_by_id(schema, prefix):
    sql = """
SELECT CONCAT( '/', TABLE_NAME, '/<id>') as route
FROM INFORMATION_SCHEMA."tables"
WHERE table_schema = %s AND table_type = 'BASE TABLE'
    AND TABLE_NAME ~ %s
ORDER BY TABLE_NAME
"""
    return db.fetchall(sql, [schema, prefix])

def get_tables_by_prefix( schema, prefix):
    sql = """
SELECT TABLE_NAME
FROM INFORMATION_SCHEMA."tables"
WHERE table_schema = %s AND table_type = 'BASE TABLE'
    AND TABLE_NAME ~ %s
"""
    return db.fetchall(sql, [schema, prefix])

def get_tables_and_columns_by_prefix( schema, prefix):
    sql = """
    SELECT t.TABLE_NAME,	string_agg(t.column_name, ',') AS COLUMN_NAMES
    FROM INFORMATION_SCHEMA."columns" t
    WHERE table_schema = %s
        AND TABLE_NAME ~ %s
    GROUP BY t.TABLE_NAME
"""
    return db.fetchall(sql, [schema, prefix])


def get_column_info( schema, table_name):
    sql = """
SELECT ORDINAL_POSITION, COLUMN_NAME, DATA_TYPE, udt_name
FROM INFORMATION_SCHEMA.COLUMNS
WHERE table_schema = %s AND TABLE_NAME = %s
"""
    return db.fetchall(sql, [schema, table_name])
