{% for table in tables %}

#######################
# {{ table.name}}
#######################

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
    WHERE id = %s
"""
    return db.fetchall(sql, [id])

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
        WHERE {{table.name}}.{{ table.columns[0]}} = t.{{ table.columns[0]}}
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
    val = [{% for col in table.columns[1:] %}
            {% if loop.index > 1 %}, {% endif %}{{table.class}}.{{ col }}{% endfor %}
        ]
    return db.execute(sql, val)


def update_{{table.name}}( {{table.name}}:{{table.class}}):
    sql = """
    UPDATE {{table.name}}
    SET {% for col in table.columns[1:] %}{% if loop.index > 1 %}, {% endif %}{{col}}=%s{% endfor %})
    WHERE {{table.columns[0]}}=%s
"""
    val = [{% for col in table.columns[1:] %}
            {% if loop.index > 1 %}, {% endif %}{{table.class}}.{{ col }}{% endfor %}
            , {{table.class}}.{{table.columns[0]}}
        ]
    return db.execute(sql, val)
{% endfor %}