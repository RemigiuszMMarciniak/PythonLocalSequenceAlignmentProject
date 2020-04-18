def string_to_array(string):
    # converts string to 1D array
    # string = string.upper()
    # index = string.rfind('\n')
    string_to_list = ""
    description = ""
    is_description_skipped = False
    for x in string:

        if x == "\n":
            is_description_skipped = True

        if is_description_skipped:
            string_to_list += x
        else:
            description += x

    # print(description)

    string_list = ""

    for x in string_to_list:
        if not x == "\n":
            # do not save
            string_list += x

    return list(string_list), description



