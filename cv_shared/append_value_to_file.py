def append_value_to_file(value, path):
    '''
    opens file to append to it
    '''
    with open(path, "a") as f:
        f.write(f"{value}\n")