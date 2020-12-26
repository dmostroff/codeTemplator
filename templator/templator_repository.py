import pgsql_db_layer as db

def get_tables_by_prefix( schema, prefix):
    sql = """
SELECT TABLE_NAME
FROM INFORMATION_SCHEMA."tables"
WHERE table_schema = %s AND table_type = 'BASE TABLE'
    AND TABLE_NAME ~ %s
"""
    return db.fetchall(sql, [schema, prefix])