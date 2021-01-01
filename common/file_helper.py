# file_helper

def write_file( file_name, text):
    with open( file_name, 'w+') as f:
        f.write( text)
    return f.closed
