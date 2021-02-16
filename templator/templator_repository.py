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
WITH t AS ( 
	SELECT c.ORDINAL_POSITION, c.TABLE_NAME, c.COLUMN_NAME, c.DATA_TYPE, c.IS_NULLABLE, COALESCE(kcu.CONSTRAINT_NAME,'') AS CONSTRAINT_NAME
	FROM INFORMATION_SCHEMA.COLUMNS c
		LEFT OUTER JOIN INFORMATION_SCHEMA.key_column_usage kcu
			ON kcu.TABLE_CATALOG = c.TABLE_CATALOG 
                AND kcu.TABLE_SCHEMA = c.TABLE_SCHEMA 
                AND kcu.TABLE_NAME = c.TABLE_NAME 
                AND kcu.COLUMN_NAME = c.COLUMN_NAME 
                AND CONSTRAINT_NAME ~ 'pkey'
    WHERE c.table_schema = %s
        AND c.TABLE_NAME ~ %s
)	
SELECT t.TABLE_NAME
    , string_agg(t.column_name, ',') AS COLUMN_NAMES
    , json_agg(t) AS COLUMN_DETAILS
FROM t
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
