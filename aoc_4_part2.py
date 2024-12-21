filename = 'aoc4data.txt'
inf = open(filename)
texts = [line.strip() for line in inf]
inf.close()

matrix = [[c for c in text] for text in texts]  # text to matrix
for e in matrix:
    print(e)

nrows = len(matrix)
ncols = len(matrix[0])

# for i in range(nrows - 2):
#     for j in range(ncols - 2):
#         if (matrix[i][j] == 'M' and matrix[i + 1][j + 1] == 'A' and matrix[i + 2][j + 2] == 'S' or
#            matrix[i][j] == 'S' and matrix[i + 1][j + 1] == 'A' and matrix[i + 2][j + 2] == 'M') and
#            (matrix[i][j + 2] == 'M' and matrix[i + 1][j + 1] == 'A' and matrix[i + 2][j] == 'S' or
#            matrix[i][j + 2] == 'S' and matrix[i + 1][j + 1] == 'A' and matrix[i + 2][j] == 'M'):
#             pass

ctr = 0
for i in range(nrows - 2):
    for j in range(ncols - 2):
        if ((matrix[i][j] == 'M' and matrix[i + 1][j + 1] == 'A' and matrix[i + 2][j + 2] == 'S' or
            matrix[i][j] == 'S' and matrix[i + 1][j + 1] == 'A' and matrix[i + 2][j + 2] == 'M') and
           (matrix[i][j + 2] == 'M' and matrix[i + 1][j + 1] == 'A' and matrix[i + 2][j] == 'S' or
            matrix[i][j + 2] == 'S' and matrix[i + 1][j + 1] == 'A' and matrix[i + 2][j] == 'M')):
            ctr += 1
print(ctr)
