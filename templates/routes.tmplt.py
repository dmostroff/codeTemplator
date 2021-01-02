import {{ group}}_service as {{group_initial}}s
{% for table in tables %}
#-- {{ table.class }}
@app.get('/{{ table.name.split('_')[0] }}/{{ '_'.join(table.name.split('_')[1:]) }}')
def get_{{table.name}} ():
    return {{group_initial}}s.get_{{table.name}}()

@app.get('/{{ table.name.split('_')[0] }}/{{ '_'.join(table.name.split('_')[1:]) }}/<id>')
def get_{{table.name}} (id):
    return {{group_initial}}s.get_{{table.name}}_by_id(id)

@app.post('/{{ table.name.split('_')[0] }}/{{ '_'.join(table.name.split('_')[1:]) }}')
def post_{{table.name}} ( {{table.name}}:{{table.class}}):
    return {{group_initial}}s.upsert_{{table.name}}({{table.name}}:{{table.class}})

{% endfor %}