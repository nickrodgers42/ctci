# Write an algorithm such that if an element in an MxN matrix is 0,
# its entire row and column are set to 0

# This one was pretty straightforward to implement, but I think it could be more efficient.

if __name__ == "__main__":
    dimensions = input().split()
    m = int(dimensions[0])
    n = int(dimensions[1])

    matrix = []

    for i in range(0, m):
        matrix.append(input().split())
    
    rows = []
    cols = []

    for i in range(0, m):
        for j in range(0, n):
            if matrix[i][j] == '0':
                rows.append(i)
                cols.append(j)
    
    for i in range(0, m):
        for j in range(0, n):
            if i in rows or j in cols:
                print('0', end=' ')
            else:
                print(matrix[i][j], end=' ')
        print()
