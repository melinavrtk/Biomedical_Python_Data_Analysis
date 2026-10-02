# =========================================================
# Chapter: Functions, Vectors, and Matrices (NumPy)
# =========================================================
import numpy as np
import random

# Function: Celsius to Fahrenheit
def c_to_f(c):
    return (9/5) * c + 32

# Function: Matrix Mean
def matrix_mean(A):
    return np.mean(A)

# Function: Filter Passing Grades
def get_passing_grades(A):
    # Extracts all grades >= 5 into a new 1D array
    A_flat = np.array(A).flatten()
    return A_flat[A_flat >= 5]

# Array Exercises (8.3a & 8.3b)
A_1d = np.array([7, 1, -2, 4, 0, 3])
print('1D Array Mean: %.1f' % np.mean(A_1d))
print('1D Array Max: %d' % np.max(A_1d))
print('1D Array Positive count: %d' % np.sum(A_1d >= 0))

A_2d = np.array([[7, 1, -2], [4, 0, 3]])
print('2D Array Mean: %.1f' % np.mean(A_2d))
print('2D Array Max: %d' % np.max(A_2d))

# Exercise 8.3f: Column Means
A_3x4 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
])
col_means = np.mean(A_3x4, axis=0)
print('Column means of 3x4 Matrix:', col_means)
