# Write a function to rotate a N x N matrix 90 degrees
# Can you do this in place?

# This one is at best an O(n^2) since we have to go through the entire 2d array
# This one was tricky for me because I had a hard time figuring out how to  
# code the movement. My approach was inline with the book.

import math

if __name__ == "__main__":
    matrixSize = int(input())
    matrix = []
    for i in range(0, matrixSize):
        matrix.append(input().split())
    
    for i in range(0, math.floor(matrixSize/2)):
        for j in range(i, matrixSize - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][matrixSize - i - 1]
            matrix[j][matrixSize - i - 1] = matrix[matrixSize - i - 1][matrixSize - j - 1]
            matrix[matrixSize - i - 1][matrixSize - j - 1] = matrix[matrixSize - j - 1][i]
            matrix[matrixSize - j - 1][i] = temp
    print()
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()       