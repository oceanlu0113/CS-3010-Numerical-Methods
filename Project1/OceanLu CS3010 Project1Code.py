# -*- coding: utf-8 -*-
"""CS3010 Project 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1De4PQM87UJqf8soEP8hAUsP6OkLOhwjQ
"""

#(A) Write a computer program to solve a linear system containing up to four equations at least using scaled partial pivoting.
#Solve the system of equations of Q. 13(a) and 13(c) , Exercise 2.2 with the program
#The output should contain,(1) Input data; (2)scale vector, index vector, pivot row no.,and multipliers at each step (3) Final Solution.

import numpy as np

def GEPP(A, b, doPricing = True):
    n = len(A)
    index = np.arange(1,n+1)
    pivot = []
    scale = np.amax(A,axis=1)
    if b.size != n:
        raise ValueError("Invalid argument: incompatible sizes between"+"A & b.", b.size, n)
    for k in range(n-1):
        print("Step:", (k+1), "Matrix\n", A)
        if doPricing:
            maxindex = abs(A[k:,k]).argmax() + k
            if A[maxindex, k] == 0:
                raise ValueError("Matrix is singular.")
            if maxindex != k:
                A[[k,maxindex]] = A[[maxindex, k]]
                b[[k,maxindex]] = b[[maxindex, k]]
                index[k], index[maxindex] = index[maxindex], index[k]
                pivot = A[maxindex]
        else:
            if A[k, k] == 0:
                raise ValueError("Pivot element is zero. Try setting doPricing to True.")
        for row in range(k+1, n):
            multiplier = A[row,k]/A[k,k]
            A[row, k:] = A[row, k:] - multiplier*A[k, k:]
            b[row] = b[row] - multiplier*b[k]
        np.arange(1,n+1)
        print("Scale: ", scale)
        print("Index:", index)
        print("Pivot:", pivot)
    x = np.zeros(n)
    for k in range(n-1, -1, -1):
        x[k] = (b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
    return x


print("Q13a:")
A = np.array([[3,4,3],
              [1,5,-1],
              [6,3,7]])
b =  np.array([[10],[7],[15]])
print("A matrix:\n", A)
print("b matrix:\n", b)
print ("Solution:\n", GEPP(A,b))

print("\nQ13c:")
A = np.array([[1,-1,2,1],
              [3,2,1,4],
              [5,8,6,3],
              [4,2,5,3]])
b =  np.array([[1],[1],[1],[-1]])
print("A matrix:\n", A)
print("b matrix:\n", b)
print ("Solution:\n", GEPP(A,b))

#(B) Write a computer program to solve a linear system (up to four equations at least) # iteration procedure of Jacobi, Gauss-Seidel and SOR Methods.
# Solve the system of equations of Q.1b and Q 2 of Computer Exercise No. 8.4 with the program. 
# The output should contain (1) Input data, (2)Successive iterates along with error check (3) Final Solution. The error bound may be taken as .000001.

import numpy as np
from scipy.linalg import solve

# Jacobi
def jacobi(A, b, x, n):
    print("\nJacobi Iterative Method")
    D = np.diag(A)
    R = A - np.diagflat(D)
    print("Step: 0  ", x)
    for i in range(n):
        x = (b - np.dot(R,x))/ D
        print("Step:", (i+1)," ", x)

# Gauss-Seidel
def gauss(A, b, x, n):
    print("\nGauss-Seidel Iterative Method")
    L = np.tril(A)
    U = A - L
    print("Step: 0  ",x)
    for i in range(n):
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        print("Step:", (i+1)," ", x)

# SOR Method
def sor(A, b, x, n, w):
    print("\nSOR Iterative Method")
    L = np.tril(A)
    U = A - L
    print("Step: 0  ",x)
    for i in range(n):
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        print("Step:", (i+1)," ", x)


        
        
        
print("Q1b: Assume omega is 1.1")
A = np.array([[5,-1,0], 
              [-1,3,-1], 
              [0,-1,2]])
b = [7,4,5]
x = [0,0,0]
n = 20
w = 1.1
print("A Matrix:\n", A)
print("b matrix\n", b)
jacobi(A, b, x, n)
gauss(A, b, x, n)
sor(A, b, x, n, w)


print("\n\nQ2")
A = np.array([[7,1,-1,2], 
              [1,8,0,-2], 
              [-1,0,4,-1],
              [2,-2,-1,6]])
b = [3,-5,4,-3]
x = [0,0,0,0]
n = 30
w = 1.1
print("A Matrix:\n", A)
print("b matrix\n", b)
jacobi(A, b, x, n)
gauss(A, b, x, n)
sor(A, b, x, n, w)