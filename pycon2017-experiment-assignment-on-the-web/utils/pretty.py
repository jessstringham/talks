# Don't mind me, just making things pretty

# Hardcoded colors for my examples.
color_map = {
    'red': 'red', 
    'blue': 'blue',
    'big': 'orange',
    'small': 'black',
}

def pp(df):
    '''A pretty print function specifically for these notebooks. Replace assignments with colors.'''
    def hl(s):
        return [
            'color: {0}; background-color: {0}'.format(color_map[v]) if v in color_map else '' 
            for v in s 
        ]
    
    return df.style.apply(hl).set_table_styles([
        {'selector': '.row_heading, .blank', 'props': [('display', 'none;')]}
    ])