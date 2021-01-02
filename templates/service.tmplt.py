import {{ group}}_repository as {{group_initial}}r
{% for table in tables %}
#--------------------
# {{table.name}}
#--------------------
def get_{{table.name}} (id):
    return {{group_initial}}r.get_{{table.name}}_by_id(id)

def post_{{table.name}} ( {{table.name}}:{{table.class}}):
    return {{group_initial}}r.upsert_{{table.name}}({{table.name}})

def put_{{table.name}} ({{table.name}}:{{table.class}}):
    return {{group_initial}}r.insert_{{table.name}}({{table.name}})

{% endfor %}