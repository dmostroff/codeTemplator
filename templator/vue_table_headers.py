import os
def create_headers(df):
    header = ['[']
    col_dict = df.to_dict("records")
    ii = 0
    for col in col_dict:
        ii += 1
        label = ' '.join(x.capitalize() or '_' for x in col['column_name'].split('_'))
        comma = ', ' if col['ordinal_position'] > 1 else ''
        header.append( "{3}{{ id: {0}, value: '{1}', text: '{2}' }}".format( col['ordinal_position'], col['column_name'], label, comma))
    header.append(']')
    return '\n'.join(header)
    


