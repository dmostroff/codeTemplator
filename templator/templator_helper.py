import os
import file_helper as fh
import vue_helper as vh
from flask import render_template
import json

def write_tables_template( prefix, df_tables, template_name, file_name):
    tables = create_tables( df_tables)
    group_name = prefix.capitalize()
    template = render_template( template_name, tables=tables, group=prefix, group_name=group_name, group_initial=prefix[:1] )
    full_name = os.path.join( os.getenv('TARGET_DIR'), file_name)
    fh.write_file( full_name, template)
    return full_name

def write_table_template( prefix, table_dict, file_name, tmplt_name):
    template = render_template( tmplt_name, table=table_dict, group=prefix, group_initial=prefix[:1] )
    full_name = os.path.join( os.getenv('TARGET_DIR'), file_name)
    fh.write_file( full_name, template)
    return full_name

def makeClassName( table_name):
    return ''.join([x.capitalize() or '_' for x in table_name.split('_')])

def makeObjectName( table_name):
    retval = ''.join([x.capitalize() or '_' for x in table_name.split('_')])
    return retval[0].lower()+retval[1:]

def makeLabelName( name):
    return ' '.join([x.capitalize() or '_' for x in name.split('_')])

def makeLabels( column_names):
    return [ makeLabelName( column) for column in column_names.split(',')]

dataTypeMapping = {
	"xid": 'str',
	"name": 'str',
	"bytea": 'bytea',
	"character": 'str',
	"date": 'datetime',
	"double precision": 'float',
	"real": 'float',
	"character varying": 'str',
	"bigint": 'int',
	"smallint": 'int',
	"boolean": 'bool',
	"integer": 'int',
	"ARRAY": 'List[str]',
	"oid": 'str',
	"numeric": 'int',
	"text": 'str',
    'timestamp with time zone': 'datetime',
    'jsonb': 'str'
}
def makeColDetails( column_details):
    for col in column_details:
        col['pydantic_type'] = dataTypeMapping[col['data_type']] if col['data_type'] in dataTypeMapping else col['data_type']
        if col['is_nullable'] == 'YES':
            col['pydantic_type'] = f"Optional[{col['pydantic_type']}] = None"
    return column_details

def create_tables( df_tables):
    table_dict = df_tables.to_dict('records')
    tables = [ 
        { 'name': row['table_name'] \
            , 'title': makeLabelName( row['table_name']) \
            , 'class': makeClassName( row['table_name']) \
            , 'object': makeObjectName( row['table_name']) \
            , 'columns': row['column_names'].split(',') \
            , 'labels': makeLabels( row['column_names']) \
            , 'column_details': makeColDetails(row['column_details']) \
            } for row in table_dict \
    ]
    return tables

def save_render( target_dir, table_name, ext, data):
    full_name = os.path.join( target_dir, table_name+"."+ext )
    fh.write_file( full_name, data)
    return full_name

def write_routes(prefix, df_tables):
    return write_tables_template( prefix, df_tables, 'routes.tmplt.py', 'main.py')

def write_resource(prefix, table_dict):
    return write_table_template( prefix, table_dict, table_dict['class'].lower()+'_resource.py', 'resource.tmplt.py')

def write_repository(prefix, df_tables):
    filename = '{0}_repository.py'.format(prefix)
    return write_tables_template( prefix, df_tables, 'repository.tmplt.py', filename)

def write_service(prefix, df_tables):
    filename = '{0}_service.py'.format(prefix)
    return write_tables_template( prefix, df_tables, 'service.tmplt.py', filename)

def write_api_js_service(prefix, df_tables):
    filename = '{0}_service.js'.format(prefix)
    return write_tables_template( prefix, df_tables, 'group_api_service.tmplt.js', filename)

def write_model(prefix, table_dict):
    return write_table_template( prefix, table_dict, table_dict['class']+'Model.py', 'model.tmplt.py')

def write_vue_table_component(prefix, table_dict):
    return write_table_template( prefix, table_dict, table_dict['class']+'.vue', 'vue_table_component.tmplt.vue')

def write_vue_detail_component(prefix, table_dict):
    return write_table_template( prefix, table_dict, table_dict['class']+'Detail.vue', 'vue_detail_component.tmplt.vue')

def write_vue_form_component(prefix, table_dict):
    return write_table_template( prefix, table_dict, table_dict['class']+'Form.vue', 'vue_form_component.tmplt.vue')
