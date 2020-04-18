import substitution_matrix_converter


def generate_optimal_local_sequence_alignment(seq1, seq2, gap_score, substitution_matrix_raw):
    print("Generate optimal local sequence")
    substitution_matrix = substitution_matrix_converter.substitution_matrix_converter(substitution_matrix_raw)
    score_matrix = [[0 for x in range(len(seq2) + 1)] for y in range(len(seq1) + 1)]
    score_matrix_displayed = [["" for x in range(len(seq2) + 2)] for y in range(len(seq1) + 2)]

    # score

    print("seq1 length " + str(len(seq1)))
    print("seq2 length " + str(len(seq2)))
    print(substitution_matrix)

    for i in range(len(score_matrix)):
        for j in range(len(score_matrix[i])):
            if i == 0 and j == 0:
                score_matrix[i][j] = 0
            else:
                if i == 0 and j > 0:
                    score_matrix[i][j] = max((j * int(gap_score)), 0)
                elif i > 0 and j == 0:
                    score_matrix[i][j] = max((i * int(gap_score)), 0)
                elif i >= 1 and j >= 1:
                    del_score = score_matrix[i - 1][j] + int(gap_score)
                    ins_score = score_matrix[i][j - 1] + int(gap_score)
                    sub_score = score_matrix[i - 1][j - 1] + match_mismatch_score(seq1[i - 1], seq2[j - 1],
                                                                                  substitution_matrix)
                    score_matrix[i][j] = max(int(del_score), int(ins_score), int(sub_score), 0)
                    print("Seq1: ", seq1[i - 1])
                    print("Seq2: ", seq2[j - 1])
                    print("match score: ", match_mismatch_score(seq1[i - 1], seq2[j - 1], substitution_matrix))
                    print(str(del_score) + " " + str(ins_score) + " " + str(sub_score))

    for x in range(len(score_matrix)):
        for y in range(len(score_matrix[x])):
            print(score_matrix[x][y], end=" ")
        print()

    for x in range(len(score_matrix_displayed)):
        for y in range(len(score_matrix_displayed[x])):
            if x == 0 and y == 0:
                score_matrix_displayed[x][y] = "#"
            if x == 0 and y == 1:
                score_matrix_displayed[x][y] = "-"
            if x == 1 and y == 0:
                score_matrix_displayed[x][y] = "-"
            elif x > 1 and y == 0:
                score_matrix_displayed[x][y] = seq1[x - 2]
            elif x == 0 and y > 1:
                score_matrix_displayed[x][y] = seq2[y - 2]
            elif x >= 1 and y >= 1:
                score_matrix_displayed[x][y] = score_matrix[x - 1][y - 1]

    for x in range(len(score_matrix_displayed)):
        for y in range(len(score_matrix_displayed[x])):
            print(score_matrix_displayed[x][y], end=" ")
        print()

    # traceback
    print("traceback")
    max_value = 0
    max_i = 0
    max_j = 0

    for x in range(len(score_matrix)):
        for y in range(len(score_matrix[x])):
            value = score_matrix[x][y]
            if value > max_value:
                max_i = x
                max_j = y
                max_value = value
                print(max_i, " ", max_j , " ", max_value)

    i_path = []
    j_path = []
    # print(score_matrix[max_i][max_j], end=" ")
    # print()
    aln1 = ""
    aln2 = ""
    while True:
        if max_i - 1 < 0 or max_j - 1 < 0:
            break
        # print(score_matrix[max_i][max_j])
        # print(max_i, " ", max_j)

        print("seq1 ", seq1[max_i - 1])
        print("seq2 ", seq2[max_j - 1])
        aln1 = seq1[max_i - 1] + aln1
        aln2 = seq2[max_j - 1] + aln2
        i_path.append(max_i)
        j_path.append(max_j)
        # <= or <
        if score_matrix[max_i - 1][max_j - 1] < 0:
            break
        max_i = max_i - 1
        max_j = max_j - 1
    print(aln1)
    print(aln2)
    # print("i path", i_path)
    # print("j path", j_path)

    identity = []

    for x in range(len(aln1)):
        if aln1[x] == aln2[x]:
            identity.append("|")
        else:
            identity.append("x")
    print("################# ####### #################")
    print("################# SUCCESS #################")
    print("################# ####### #################")
    print("Path has been generated succesfully.")
    print("aln1: " + str(aln1))
    print("      " + str("".join(identity)))
    print("aln2: " + str(aln2))
    print("i path: " + str(i_path))
    print("j path: " + str(j_path))

    optimal_path = aln1 + '\n' + "".join(identity) + '\n' + aln2
    return score_matrix, optimal_path, i_path, j_path, score_matrix_displayed,aln1,aln2


def match_mismatch_score(seq1, seq2, substitution_matrix):
    sub_score = 0
    if seq1 == "A":
        if seq2 == "A":
            sub_score = substitution_matrix[0][0]
        elif seq2 == "C":
            sub_score = substitution_matrix[0][1]
        elif seq2 == "G":
            sub_score = substitution_matrix[0][2]
        elif seq2 == "T" or seq2 == "U":
            sub_score = substitution_matrix[0][3]
    elif seq1 == "C":
        if seq2 == "A":
            sub_score = substitution_matrix[1][0]
        elif seq2 == "C":
            sub_score = substitution_matrix[1][1]
        elif seq2 == "G":
            sub_score = substitution_matrix[1][2]
        elif seq2 == "T" or seq2 == "U":
            sub_score = substitution_matrix[1][3]
    elif seq1 == "G":
        if seq2 == "A":
            sub_score = substitution_matrix[2][0]
        elif seq2 == "C":
            sub_score = substitution_matrix[2][1]
        elif seq2 == "G":
            sub_score = substitution_matrix[2][2]
        elif seq2 == "T" or seq2 == "U":
            sub_score = substitution_matrix[2][3]
    elif seq1 == "T" or seq1 == "U":
        if seq2 == "A":
            sub_score = substitution_matrix[3][0]
        elif seq2 == "C":
            sub_score = substitution_matrix[3][1]
        elif seq2 == "G":
            sub_score = substitution_matrix[3][2]
        elif seq2 == "T" or seq2 == "U":
            sub_score = substitution_matrix[3][3]

    print("subscore: ", sub_score)
    return sub_score

    #

    #
    # aln1 = ""
    # aln2 = ""
    # i = len(score_matrix) - 1
    # j = len(score_matrix[0]) - 1
    #
    # # print(str(i) + " i , j " + str(j))
    # # print()
    # # print(str(len(seq1)) + " len seq1 , len seq2 " + str(len(seq2)))
    #
    # i_path = []
    # j_path = []
    #
    # while True:
    #     print(str(i_path) + "<ipath jpath> " + str(j_path))
    #     if i == 0 and j == 0:
    #         i_path.append(i)
    #         j_path.append(j)
    #         break
    #     if j == 0:
    #         aln2 = "-" + aln2
    #         aln1 = seq1[i - 1] + aln1
    #         i_path.append(i)
    #         j_path.append(j)
    #         i = i - 1
    #         continue
    #     if i == 0:
    #         aln2 = seq2[j - 1] + aln2
    #         aln1 = "-" + aln1
    #         i_path.append(i)
    #         j_path.append(j)
    #         j = j - 1
    #         continue
    #     # print(str(i) + " i , j " + str(j))
    #     # print("score for i and j : " + str(score_matrix[i][j]))
    #     # print("score for i-1 and j-1 : " + str(score_matrix[i-1][j-1]))
    #     # print("score for i-1 and j : " + str(score_matrix[i-1][j]))
    #     # print("score for i and j-1 : " + str(score_matrix[i][j-1]))
    #
    #     del_score = score_matrix[i - 1][j]
    #     ins_score = score_matrix[i][j - 1]
    #     sub_score = score_matrix[i - 1][j - 1]
    #     minimum_score = min(del_score, ins_score, sub_score)
    #     print(str(del_score), str(ins_score), str(sub_score))
    #     print(minimum_score)
    #     # print("##############")
    #     # print(del_score)
    #     # print(ins_score)
    #     # print(sub_score)
    #     # print(minimum_score)
    #     # print("##############")
    #     # print("aln1: " + str(aln1))
    #     # print("aln2: " + str(aln2))
    #
    #     if minimum_score == sub_score:
    #         aln1 = seq1[i - 1] + aln1
    #         aln2 = seq2[j - 1] + aln2
    #         i_path.append(i)
    #         j_path.append(j)
    #         i = i - 1
    #         j = j - 1
    #     else:
    #         if minimum_score == del_score:
    #             aln2 = "-" + aln2
    #             aln1 = seq1[i - 1] + aln1
    #             i_path.append(i)
    #             j_path.append(j)
    #             i = i - 1
    #         else:
    #             aln2 = seq2[j - 1] + aln2
    #             aln1 = "-" + aln1
    #             i_path.append(i)
    #             j_path.append(j)
    #             j = j - 1
    #
    #     # print("aln1: " + str(aln1))
    #     # print("aln2: " + str(aln2))
    #
    #     identity = []
    #     for x in range(len(aln1)):
    #         if aln1[x] == aln2[x]:
    #             identity.append("|")
    #         else:
    #             identity.append("x")
    #     print("################# ####### #################")
    #     print("################# SUCCESS #################")
    #     print("################# ####### #################")
    #     print("Path has been generated succesfully.")
    #     print("aln1: " + str(aln1))
    #     print("      " + str("".join(identity)))
    #     print("aln2: " + str(aln2))
    #     print("i path: " + str(i_path))
    #     print("j path: " + str(j_path))
    #
    #     # while i >= 0 and j >= 0:
    #     #     print(str(i) + " i , j " + str(j))
    #     #     print("score for i and j : " + str(score_matrix[i][j]))
    #     #     if i == 0 and j == 0:
    #     #         break
    #     #     else:
    #     #         if i > 0 and j > 0 and (score_matrix[i][j] == score_matrix[i - 1][j - 1] + int(mismatch_score) * (
    #     #                     seq1[i - 1] != seq2[j - 1])):
    #     #             aln1 = seq1[i - 1] + aln1
    #     #             aln2 = seq2[j - 1] + aln2
    #     #             i = i - 1
    #     #             j = j - 1
    #     #         else:
    #     #             if i > 0 and (score_matrix[i][j] == score_matrix[i-1][j] + int(gap_score)):
    #     #                 aln1 = "-" + aln1
    #     #                 aln2 = seq2[j-1] + aln2
    #     #                 j = j - 1
    #     #             elif j > 0 and (score_matrix[i][j] == score_matrix[i][j-1] + int(gap_score)):
    #     #                 aln1 = seq1[i-1] + aln1
    #     #                 aln2 = "-" + aln2
    #     #                 i = i - 1
    #
    # else:
    #     # generate V table for Needleman-Wunsh algorithm (mode similiarity)
    #     for i in range(len(score_matrix)):
    #         for j in range(len(score_matrix[i])):
    #             if i == 0 and j == 0:
    #                 score_matrix[i][j] = 0
    #             else:
    #                 if i == 0 and j > 0:
    #                     score_matrix[i][j] = j * int(gap_score)
    #                 elif i > 0 and j == 0:
    #                     score_matrix[i][j] = i * int(gap_score)
    #                 elif i >= 1 and j >= 1:
    #                     del_score = score_matrix[i - 1][j] + int(gap_score)
    #                     ins_score = score_matrix[i][j - 1] + int(gap_score)
    #                     sub_score = score_matrix[i - 1][j - 1] + int(
    #                         int(mismatch_score) * bool(seq1[i - 1] != seq2[j - 1]))
    #                     if seq1[i - 1] == seq2[j - 1]:
    #                         reward_score = score_matrix[i - 1][j - 1] + int(
    #                             int(match_score))
    #                         # print(str(del_score) + " " + str(ins_score) + " " + str(sub_score) + " " + str(reward_score))
    #                         score_matrix[i][j] = max(int(del_score), int(ins_score), int(sub_score),
    #                                                  int(reward_score))
    #                         continue
    #                     # print(str(del_score) + " " + str(ins_score) + " " + str(sub_score))
    #                     score_matrix[i][j] = max(int(del_score), int(ins_score), int(sub_score))
    #
    #     # for x in range(len(score_matrix)):
    #     #     for y in range(len(score_matrix[x])):
    #     #         print(score_matrix[x][y], end=" ")
    #     #     print()
    #
    #     for x in range(len(score_matrix_displayed)):
    #         for y in range(len(score_matrix_displayed[x])):
    #             if x == 0 and y == 0:
    #                 score_matrix_displayed[x][y] = "#"
    #             if x == 0 and y == 1:
    #                 score_matrix_displayed[x][y] = "-"
    #             if x == 1 and y == 0:
    #                 score_matrix_displayed[x][y] = "-"
    #             elif x > 1 and y == 0:
    #                 score_matrix_displayed[x][y] = seq1[x - 2]
    #             elif x == 0 and y > 1:
    #                 score_matrix_displayed[x][y] = seq2[y - 2]
    #             elif x >= 1 and y >= 1:
    #                 score_matrix_displayed[x][y] = score_matrix[x - 1][y - 1]
    #
    #     for x in range(len(score_matrix_displayed)):
    #         for y in range(len(score_matrix_displayed[x])):
    #             print(score_matrix_displayed[x][y], end=" ")
    #         print()
    #
    #     aln1 = ""
    #     aln2 = ""
    #     i = len(score_matrix) - 1
    #     j = len(score_matrix[0]) - 1
    #     #
    #     # print(str(i) + " i , j " + str(j))
    #     # print()
    #     # print(str(len(seq1)) + " len seq1 , len seq2 " + str(len(seq2)))
    #
    #     i_path = []
    #     j_path = []
    #
    #     while i >= 0 and j >= 0:
    #         if i == 0 and j == 0:
    #             i_path.append(i)
    #             j_path.append(j)
    #             break
    #
    #         # print(str(i) + " i , j " + str(j))
    #         # print("score for i and j : " + str(score_matrix[i][j]))
    #         # print("score for i-1 and j-1 : " + str(score_matrix[i-1][j-1]))
    #         # print("score for i-1 and j : " + str(score_matrix[i-1][j]))
    #         # print("score for i and j-1 : " + str(score_matrix[i][j-1]))
    #
    #         del_score = score_matrix[i - 1][j]
    #         ins_score = score_matrix[i][j - 1]
    #         sub_or_reward_score = score_matrix[i - 1][j - 1]
    #         maximum_score = max(del_score, ins_score, sub_or_reward_score)
    #         # print("##############")
    #         # print(del_score)
    #         # print(ins_score)
    #         # print(sub_or_reward_score)
    #         # print(maximum_score)
    #         # print("##############")
    #         # print("aln1: " + str(aln1))
    #         # print("aln2: " + str(aln2))
    #
    #         if maximum_score == sub_or_reward_score:
    #             aln1 = seq1[i - 1] + aln1
    #             aln2 = seq2[j - 1] + aln2
    #             i_path.append(i)
    #             j_path.append(j)
    #             i = i - 1
    #             j = j - 1
    #         else:
    #             if maximum_score == del_score:
    #                 aln2 = "-" + aln2
    #                 aln1 = seq1[i - 1] + aln1
    #                 i_path.append(i)
    #                 j_path.append(j)
    #                 i = i - 1
    #             else:
    #                 aln2 = seq2[j - 1] + aln2
    #                 aln1 = "-" + aln1
    #                 i_path.append(i)
    #                 j_path.append(j)
    #                 j = j - 1
    #
    #         # print("aln1: " + str(aln1))
    #         # print("aln2: " + str(aln2))
    #
    #     identity = []
    #     for x in range(len(aln1)):
    #         if aln1[x] == aln2[x]:
    #             identity.append("|")
    #         else:
    #             identity.append("x")
    #     print("################# ####### #################")
    #     print("################# SUCCESS #################")
    #     print("################# ####### #################")
    #     print("Path has been generated succesfully.")
    #     print("aln1: " + str(aln1))
    #     print("      " + str("".join(identity)))
    #     print("aln2: " + str(aln2))
    #     print("i path: " + str(i_path))
    #     print("j path: " + str(j_path))
    #
    # # statistics
    # # match
    # length = max(len(aln1), len(aln2))
    # score = 0
    # identity_count = 0
    # gaps_count = 0
    # for x in range(len(aln1)):
    #     if aln1[x] != aln2[x]:
    #         score = score + 1
    #     if aln1[x] == aln2[x]:
    #         identity_count = identity_count + 1
    #     if aln1[x] == "-":
    #         gaps_count = gaps_count + 1
    #     if aln2[x] == "-":
    #         gaps_count = gaps_count + 1
    #
    # optimal_path = aln1 + '\n' + "".join(identity) + '\n' + aln2
    # return score_matrix, score, length, identity_count, gaps_count, optimal_path, i_path, j_path
