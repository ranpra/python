"""
Vector
A vector is an ordered collection of scalars. It can be represented in two forms:

1. Column vector: Contains n rows and 1 column
2. Row vector: contains 1 row and n columns

The number of scalars in a vector is called its dimension or order.

"""
import numpy as np
col_vec=np.array([[4],[3]])
print("A column vector\n",col_vec)
print("Shape of vector=",col_vec.shape)

row_vec = np.array([4,-1,2])
print("A row vector\n",row_vec)
print("Shape of vector=",row_vec.shape)


#Illustrating a Zero row vector of dimension 3 using np.array() function
zero_vector_1=np.array([0,0,0])
print(zero_vector_1)
#Illustrating a Zero row vector of dimension 3 using np.zeros() function
zero_vector_2=np.zeros(3)
print(zero_vector_2)
#Illustrating a Zero column vector of dimension 3 using np.zeros() and reshape() function
zero_vector_3=np.zeros(3).reshape(3,-1)
print(zero_vector_3)

#Illustrating a One vector of dimension 3 using np.array() function
one_vector_1=np.array([1,1,1])
print(one_vector_1)
#Illustrating a One vector of dimension 3 using np.ones() function
one_vector_2=np.ones(3)
print(one_vector_2)
#Illustrating a column vector of ones of dimension 3 using np.ones() and reshape() function 
one_vector_3=np.ones(3).reshape(3,-1)
print(one_vector_3)

vector=np.array([[4],[-1],[2]])
print("The vector\n",vector)
#Addressing a value of vector by index
print("\nElement at position 1=",vector[1])

#Create a vector
vector=np.array([3,3])
#Magnitude of vector can be found using function np.linalg.norm() function
print("\nMagnitude of the vector = ",np.linalg.norm(vector))