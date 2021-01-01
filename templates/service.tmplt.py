import {{ group}}_repository as {{group_initial}}r
{% for table in tables %}

def get_{{table.name}}():
    sql = """
    SELECT {{table.columns}}
    FROM {{table.name}}
"""
    return db.fetchall(sql)

def get_{{table.name}}_by_id(id):
    sql = """
    SELECT {{table.columns}}
    FROM {{table.name}}
"""
    return db.fetchall(sql, [id])

def insert_{{table.name}}( {{table.name}}:{{table.class}}):
    sql = """
    INSERT INTO {{table_name}}( 
        {% for col in table.columns %}
            {% if loop.index > 1 %}, {% endif %}{{ col }}
        {% endfor %}
        )
    VALUES( 
        {% for col in table.columns %}
            {% if loop.index > 1 %}, {% endif %}{{table.class}}.{{col}}
        {% endfor %}
        )
"""
    return db.fetchall(sql, [id])
    
@app.get('/{{ table.name }}/<id>')
def get_{{table.name}} (id):
    return {{group_initial}}s.get_{{table.name}}_by_id(id)

@app.post('/{{ table.name }}/')
def post_{{table.name}} ( {{table.name}}:{{table.class}}):
    return {{group_initial}}s.create_{{table.name}}({{table.name}}:{{table.class}})

@app.put('/{{ table.name }}/')
def put_{{table.name}} ({{table.name}}:{{table.class}}):
    return {{group_initial}}s.update_{{table.name}}({{table.name}})

{% endfor %}