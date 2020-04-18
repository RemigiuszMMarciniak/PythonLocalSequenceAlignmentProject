def read_file(file_name):
    with open(file_name) as file_object:
        contents = file_object.read()
        return contents


