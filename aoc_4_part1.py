def transpose_text(texts):
    matrix = [[texts[j][i] for j in range(len(texts))] for i in range(len(texts))]
    return [''.join([item for item in e]) for e in matrix]


# todo: move transpose_text to pythontools, document properly

filename = 'aoc4data.txt'
inf = open(filename)
texts = [line.strip() for line in inf]
inf.close()

###############################################################################
# horizontal
print(sum([text.count('XMAS') for text in texts]))
print(sum([text.count('SAMX') for text in texts]))  # reverse search

hmatrix = [[c for c in text] for text in texts]  # text to matrix
hmatrix_rev = [list(reversed(e)) for e in hmatrix]

###############################################################################
# vertical
# vmatrix = [[texts[j][i] for j in range(len(texts))] for i in range(len(texts))]
# vtexts = [''.join([item for item in e]) for e in vmatrix]  # matrix to text

vtexts = transpose_text(texts)
print(sum([s.count('XMAS') for s in vtexts]))
print(sum([s.count('SAMX') for s in vtexts]))  # reverse search


################################################################################
# diagonal - going up left to right  - northeast
def create_diag_matrix(matrix):
    nrows = len(matrix)
    ncols = len(matrix[0])
    diag_matrix = []

    start1 = [[i, 0] for i in range(nrows)]
    for i, j in start1:
        line = []
        for k in range(nrows + 1):
            # print(i, j)
            line.append(matrix[i][j])
            if i == 0:
                break
            i -= 1
            j += 1
        diag_matrix.append(line)

    start2 = [[ncols - 1, j] for j in range(1, ncols)]
    for i, j in start2:
        line = []
        for k in range(ncols - 1):
            # print(i, j)
            line.append(matrix[i][j])
            if j == ncols - 1:
                break
            i -= 1
            j += 1
        diag_matrix.append(line)
    return diag_matrix


diag_matrix1 = create_diag_matrix(hmatrix)
diag_texts1 = [''.join([item for item in e]) for e in diag_matrix1]  # matrix to text

print(sum([s.count('XMAS') for s in diag_texts1]))
print(sum([s.count('SAMX') for s in diag_texts1]))  # reverse search

diag_matrix2 = create_diag_matrix(hmatrix_rev)
diag_texts2 = [''.join([item for item in e]) for e in diag_matrix2]  # matrix to text

print(sum([s.count('XMAS') for s in diag_texts2]))
print(sum([s.count('SAMX') for s in diag_texts2]))  # reverse search

# 179
# 211
# 205
# 199
# 436
# 406
# 395
# 366
