from flask_restful import Resource
import {{ group}}_service as {{group_initial}}s

class {{ table.class}}s(Resource):
    def get(self):
        return {{group_initial}}s.get_{{table.name}}()

class {{ table.class}}(Resource):
    def get(self, id):
        return {{group_initial}}s.get_{{table.name}}(id)

class {{ table.class}}Post(Resource):
    def post(self, id):
        {{table.name}} = {{tabke,class}}JsonToModel(request.get_json())
        return ars.upsert_{{table_name}}( {{table_name}})
