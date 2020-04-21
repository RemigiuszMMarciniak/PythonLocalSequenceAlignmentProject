import matplotlib.pyplot as plt
import numpy as np


def save_to_graph(score_matrix, i_path, j_path, score_table_file_name, seq1, seq2):
    N = len(score_matrix[0])
    M = len(score_matrix)
    path_matrix = [[0] * N for _ in range(M)]
    for x in range(len(path_matrix)):
        for y in range(len(path_matrix[x])):
            for z in range(len(i_path)):
                if i_path[z] == x and j_path[z] == y:
                    path_matrix[x][y] = 1
    plt.figure()
    description_first = str("".join(seq2[:9]))
    description_second = str("".join(seq1[:9]))
    if len(seq1) > 10:
        plt.ylabel(str(description_second) + '...')
    else:
        plt.ylabel(str(description_second))
    if len(seq2) > 10:
        plt.xlabel(str(description_first) + '...')
    else:
        plt.xlabel(str(description_first))
    plt.title("Path")
    H = np.array(path_matrix)
    plt.imshow(H)
    plt.savefig(score_table_file_name + '.png')
