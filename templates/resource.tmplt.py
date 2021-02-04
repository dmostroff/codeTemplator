from flask_restful import Resource
import {{ group}}_service as {{group_initial}}s

{{ table.object}} = {}
class {{ table.class}}s(Resource):
    def get(self):
        return {{group_initial}}s.get_{{table.name}}()

class {{ table.class}}(Resource):
    def get(self, id):
        return {{group_initial}}s.get_{{table.name}}(id)

    def put(self, id):
        {{ table.object }}[id] = request.form['{{table.object}}']
        return {{ '{' }}'{{table.object}}_id': {{table.object}}[id]{{ '}'}}