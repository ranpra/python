"""
Matrix
A matrix is defined as a rectangular array of numbers. It consists of rows and columns. 

The number of rows (m) and columns (n) is defined as the dimension or order of the matrix and is represented as (m, n). A matrix is called a square matrix if the number of rows(m) is equal to the number of columns(n).

Using the library NumPy, you can create matrices of different orders as shown below:
"""
# importing required libraries (numpy as np)
import numpy as np
# Creating matrices of various dimension using np.array() function
matrix_2x2 = np.array([[1, 2], 
                       [3, 4]])
matrix_3x3 = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [8, 9, 10]])
print("2x2 Matrix\n",matrix_2x2,"\nshape of matrix -> ",matrix_2x2.shape)
print("\n3x3 Matrix\n",matrix_3x3,"\nshape of matrix -> ",matrix_3x3.shape)

# Creating a 3x2 Matrix "A"
A = np.array([[2,-2],[3,1],[1,4]])
#selecting an element at row index 2 and column index 1
print("Element of matrix A at index position [2,1] is", A[2,1])

# Creating a 3x2 Matrix "A"
A = np.array([[2,-2],[3,1],[1,4]])
print("Matrix A:\n",A)
# Finding transpose of a matrix using the function transpose()
print("Matrix A Transpose: \n",np.transpose(A))

