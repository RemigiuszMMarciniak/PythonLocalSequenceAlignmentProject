def substitution_matrix_converter(substitution_matrix_raw):
    # print(substitution_matrix_raw)
    # print(list(substitution_matrix_raw))
    substitution_matrix = [[0 for x in range(4)] for y in range(4)]
    substitution_matrix_line = substitution_matrix_raw[0]
    len_substitution_matrix_line = len(substitution_matrix_line)
    substitution_matrix_line = str(substitution_matrix_line)
    substitution_matrix_line = substitution_matrix_line \
        .replace("\'", "") \
        .replace(" ", "") \
        .replace("A", "") \
        .replace("T", "") \
        .replace("U", "") \
        .replace("G", "") \
        .replace("C", "") \
        .replace(",", "") \
        .replace("[", "") \
        .replace("]", "")

    substitution_matrix_line = list(substitution_matrix_line)
    substitution_matrix_line_int_from_string = [0 for x in range(16)]
    # print()
    # print(substitution_matrix_line)
    index = 0
    x = len(substitution_matrix_line) - 1
    was_below_zero = False
    for x in range(len(substitution_matrix_line)):
        # print(substitution_matrix_line[x],end= " ")
        if was_below_zero:
            was_below_zero = False
            continue
        else:
            if substitution_matrix_line[x] == "-":
                substitution_matrix_line_int_from_string[index] = -1 * int(substitution_matrix_line[x + 1])
                index = index + 1
                was_below_zero = True
            else:
                substitution_matrix_line_int_from_string[index] = int(substitution_matrix_line[x])
                index = index + 1
    print("sub matrix from string", substitution_matrix_line_int_from_string)
    z = 0
    for x in range(len(substitution_matrix)):
        for y in range(len(substitution_matrix[0])):
            substitution_matrix[x][y] = substitution_matrix_line_int_from_string[z]
            z = z + 1
    print("sub matrix",substitution_matrix)
    return substitution_matrix
