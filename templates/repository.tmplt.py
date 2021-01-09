import pgsql_db_layer as db

{% for table in tables %}
#######################
# {{ table.name}}
#######################
import {{table.class}}

def get_{{table.name}}():
    sql = """
    SELECT {{','.join(table.columns)}}
    FROM {{table.name}}
"""
    return db.fetchall(sql)

def get_{{table.name}}_by_id(id):
    sql = """
    SELECT {{ ','.join(table.columns)}}
    FROM {{table.name}}
    WHERE {% for col in table.column_details %}{% if col.constraint_name > '' %}{% if loop.index > 1 %} AND{% endif %}{{ col.column_name}} = %s{% endif %}{% endfor %}
"""
    return db.fetchall(sql, [id])

def get_{{table.name}}_by_{{group}}_id({{group}}_id):
    sql = """
    SELECT {{ ','.join(table.columns)}}
    FROM {{table.name}}
    WHERE {{group}}_id = %s
"""
    return db.fetchall(sql, [{{group}}_id])

def upsert_{{table.name}}( {{table.name}}:{{table.class}}):
    sql = """
    WITH t AS (
        SELECT {% for col in table.columns %}
            {% if loop.index > 1 %}, {% endif %}%s as {{col}}{% endfor %}
    ),
    u AS (
        UPDATE {{table.name}}
        SET {% for col in table.columns[1:] %}
            {% if loop.index > 1 %}, {% endif %}{{col}}=t.{{col}}{% endfor %}
        FROM t
        WHERE {% for col in table.column_details %}{% if col.constraint_name > '' %}{% if loop.index > 1 %} AND{% endif %}{{table.name}}.{{ col.column_name}} = t.{{ col.column_name}}{% endif %}{% endfor %}
        RETURNING {{ table.columns[0]}}
    ),
    i AS (
        INSERT INTO {{table.name}}( {{ ','.join(table.columns[1:])}})
        SELECT {% for col in table.columns[1:] %}
            {% if loop.index > 1 %}, {% endif %}t.{{col}}{% endfor %}
        FROM t
        WHERE NOT EXISTS ( SELECT 1 FROM u)
    )
    SELECT 'INSERT' as ACTION, {{ table.columns[0]}}
    FROM i
    UNION ALL
    SELECT 'UPDATE' as ACTION, {{ table.columns[0]}}
    FROM u
    ;
    ;
"""
    val = [{% for col in table.columns %}
            {% if loop.index > 1 %}, {% endif %}{{table.class}}.{{ col }}{% endfor %}
        ]
    return db.execute(sql, val)

def insert_{{table.name}}( {{table.name}}:{{table.class}}):
    sql = """
    INSERT INTO {{table.name}}( {{ ','.join(table.columns[1:])}})
    VALUES ({% for col in table.columns[1:] %}{% if loop.index > 1 %}, {% endif %}%s{% endfor %})
    ;
"""
    val = [{% for col in table.column_details %}
            {% if col.constraint_name == '' %}{% if loop.index > 2 %}, {% endif %}{{table.class}}.{{ col.column_name}}{% endif %}{% endfor %}
        ]
    return db.execute(sql, val)

# this has a flaw in loop.index > 2
def update_{{table.name}}( {{table.name}}:{{table.class}}):
    sql = """
    UPDATE {{table.name}}
    SET {% for col in table.column_details %}{% if col.constraint_name == '' %}{% if loop.index > 2 %}, {% endif %}{{ col.column_name}} = %s{% endif %}{% endfor %}
    WHERE {% for col in table.column_details %}{% if col.constraint_name > '' %}{% if loop.index > 1 %} AND{% endif %}{{ col.column_name}} = %s{% endif %}{% endfor %}
"""
    val = [{% for col in table.column_details %}{% if col.constraint_name == '' %}{% if loop.index > 2 %}
            , {% endif %}{{table.class}}.{{ col.column_name}}{% endif %}{% endfor %}
        {% for col in table.column_details %}
            {% if col.constraint_name > '' %}, {{table.class}}.{{ col.column_name}}{% endif %}{% endfor %}            
        ]
    return db.execute(sql, val)
{% endfor %}