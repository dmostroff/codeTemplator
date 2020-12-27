
def write_file( file_name, text):
    with open( file_name, 'w') as f:
        for line in text:
            f.write( line)
    return f.closed
