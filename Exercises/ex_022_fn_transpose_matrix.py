def transpose_of_matrix(matrix):
    row1 = []
    row2 = []
    row3 = []
    for row in matrix:
        row1.append(row[0])
        row2.append(row[1])
        row3.append(row[2])
    transpose_matrix = [row1, row2, row3]
    for row in transpose_matrix:
        print(row)

#matrix = [
#[1, 2, 3],
#[4, 5, 6],
#[7, 8, 9]
#]
# transpose_of_matrix(matrix)
