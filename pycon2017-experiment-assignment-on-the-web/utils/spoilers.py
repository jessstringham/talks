import hashlib


def hash_func(input_str):
    hash_hex = hashlib.md5(input_str.encode('utf-8')).hexdigest()
    return int(hash_hex[:15], 16)

# Alias
spoiler_hash_func = hash_func

def choose_color_assignment(user_id):
    key = "{}|color".format(user_id)

    slot = spoiler_hash_func(key) % 20
    
    if slot < 10:
        return 'red'
    else:
        return 'blue'