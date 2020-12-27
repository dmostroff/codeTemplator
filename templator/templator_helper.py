import os
import file_helper as fh


def read_and_render( template_name):
    template = Template()

def save_render( target_dir, table_name, ext, data):
    full_name = os.path.join( target_dir, table_name+"."+ext )
    fh.write_file( full_name, data)
    return full_name
