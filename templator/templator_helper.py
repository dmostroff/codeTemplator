import os
import file_helper as fh
import vue_helper as vh
from flask import render_template

def makeClassName( table_name):
    return ''.join([x.capitalize() or '_' for x in table_name.split('_')])

def makeObjectName( table_name):
    retval = ''.join([x.capitalize() or '_' for x in table_name.split('_')])
    return retval[0].lower()+retval[1:]

def makeLabelName( name):
    return ' '.join([x.capitalize() or '_' for x in name.split('_')])

def makeLabels( column_names):
    return [ makeLabelName( column) for column in column_names.split(',')]


def create_tables( df_tables):
    table_dict = df_tables.to_dict('records')
    tables = [ 
        { 'name': row['table_name'] \
            , 'title': makeLabelName( row['table_name']) \
            , 'class': makeClassName( row['table_name']) \
            , 'object': makeObjectName( row['table_name']) \
            , 'columns': row['column_names'].split(',') \
            , 'labels': makeLabels( row['column_names']) \
            } for row in table_dict \
    ]
    return tables

def instantiate_template( prefix, df_tables, template_name, file_name):
    tables = create_tables( df_tables)
    template = render_template( template_name, tables=tables, group=prefix, group_initial=prefix[:1] )
    full_name = os.path.join( os.getenv('TARGET_DIR'), file_name)
    fh.write_file( full_name, template)
    return full_name

def save_render( target_dir, table_name, ext, data):
    full_name = os.path.join( target_dir, table_name+"."+ext )
    fh.write_file( full_name, data)
    return full_name

def write_routes(prefix, df_tables):
    return instantiate_template( prefix, df_tables, 'routes.tmplt.py', 'app.py')

def write_repository(prefix, df_tables):
    filename = '{0}_repository.py'.format(prefix)
    return instantiate_template( prefix, df_tables, 'repository.tmplt.py', filename)

def write_service(prefix, df_tables):
    filename = '{0}_service.py'.format(prefix)
    return instantiate_template( prefix, df_tables, 'service.tmplt.py', filename)

def write_api_js_service(prefix, df_tables):
    filename = '{0}_service.js'.format(prefix)
    return instantiate_template( prefix, df_tables, 'group_api_service.tmplt.js', filename)

def write_vue_component(prefix, table_dict):
    filename = '{0}.vue'.format(table_dict['class'])
    # headers = vh.create_headers( table_dict)
    template = render_template( 'vue_component.tmplt.vue', table=table_dict, group=prefix, group_initial=prefix[:1] )
    full_name = os.path.join( os.getenv('TARGET_DIR'), filename)
    fh.write_file( full_name, template)
    return full_name
