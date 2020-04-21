def save_score_table_and_optimal_path_to_files(pptimal_path,score_matrix,score_matrix_displayed,seq1,seq2,aln1,aln2,
                                               label1,label2,i_path,j_path,path_file_name,score_table_file_name):
    identity = []

    for x in range(len(aln1)):
        if aln1[x] == aln2[x]:
            identity.append("|")
        else:
            identity.append("x")
    # print("################# ####### #################")
    # print("################# SUCCESS #################")
    # print("################# ####### #################")
    # print("Path has been generated succesfully.")
    # print("aln1: " + str(aln1))
    # print("      " + str("".join(identity)))
    # print("aln2: " + str(aln2))
    # print("i path: " + str(i_path))
    # print("j path: " + str(j_path))

    optimal_path = aln1 + '\n' + "".join(identity) + '\n' + aln2

    description = ">seq1 " + str("".join(label1)) + '\n' + \
                    str(seq1) + '\n' + \
                  ">seq2 " + str("".join(label2)) + '\n' + \
                    str(seq2) + '\n' + ">optimal path " + '\n' + optimal_path
    # print(description)
    f = open(path_file_name + "_optimal_path.fasta", "w+")
    f.write(description)
    f.close()

    score_table_raw = [["" for x in range(len(score_matrix[0]) + 1)] for y in range(len(score_matrix) + 1)]

    # print(len(score_matrix))
    # print(len(score_matrix[0]))
    # print(len(score_table_raw))
    # print(len(score_table_raw[0]))
    # print(score_table_raw)
    # print(score_matrix)

    # print("len score matrix " + str(len(score_matrix)))
    # print("len score raw table " + str(len(score_table_raw)))
    for x in range(len(score_matrix)):
        for y in range(len(score_matrix[x])):
            # print("x, y " + str(x) + " , " + str(y))
            score_table_raw[x][y] = score_matrix[x][y]
            for z in range(len(i_path)):
                if i_path[z] == x and j_path[z] == y:
                    score_table_raw[x][y] = str(score_table_raw[x][y]) + "*"

    # print("ipath: " + str(i_path))
    # print("jpath: " + str(j_path))

    # for x in range(len(score_table_raw)):
    #     for y in range(len(score_table_raw[x])):
    #         print(score_table_raw[x][y], end=" ")
    #     print()

    score_matrix_to_be_shown = [["" for x in range(len(score_table_raw[0]) + 1)] for y in
                                range(len(score_table_raw) + 1)]
    # print(len(score_table_raw))
    # print(len(score_table_raw[0]))
    for x in range(len(score_table_raw)):
        for y in range(len(score_table_raw[0])):
            # print(str(x) + " x , y " + str(y))
            if x == 0 and y == 0:
                score_matrix_to_be_shown[x][y] = "#"
            if x == 0 and y == 1:
                score_matrix_to_be_shown[x][y] = "-"
            if x == 1 and y == 0:
                score_matrix_to_be_shown[x][y] = "-"
            elif x > 1 and y == 0:
                score_matrix_to_be_shown[x][y] = seq1[x - 2]
            elif x == 0 and y > 1:
                score_matrix_to_be_shown[x][y] = seq2[y - 2]
            elif x >= 1 and y >= 1:
                score_matrix_to_be_shown[x][y] = score_table_raw[x - 1][y - 1]
    score_matrix_to_string = ""
    for x in range(len(score_matrix_to_be_shown)):
        for y in range(len(score_matrix_to_be_shown[x])):
            # print(score_matrix_to_be_shown[x][y], end=" ")
            score_matrix_to_string = score_matrix_to_string + str(score_matrix_to_be_shown[x][y]) + " "
        # print()
        score_matrix_to_string = score_matrix_to_string + '\n'

    f = open(score_table_file_name + "_score_table.txt", "w+")
    f.write(str(score_matrix_to_string))
    f.close()
