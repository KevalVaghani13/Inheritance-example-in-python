###1.1
import numpy as np
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6],[7,8,9]])

# print("1-D array dimensions:", array_1d.ndim)
# print("2-D array dimensions:", array_2d.ndim)


###1.2
# array_1d = np.array([1, 2, 3, 4, 5])
# array_2d = np.array([[1, 2, 3],
#                      [4, 5, 6],
#                      [7, 8, 9]])

# print("1-D array size:", array_1d.size)
# print("2-D array size:", array_2d.size)


###1.3
# array_1d = np.array([1, 2, 3, 4, 5])
# array_2d = np.array([[1, 2, 3],
#                      [4, 5, 6],
#                      [7, 8, 9]])

# print("1-D array shape:", array_1d.shape)
# print("2-D array shape:", array_2d.shape)


###2.1
# import numpy as np
# 1- D array 
arr_addition = array_1d + array_1d 
arr_subtraction = array_1d - array_1d 
arr_multiplication = array_1d * array_1d 
print("Array Addition (1-D):", arr_addition) 
print("Array Subtraction (1-D):", arr_subtraction) 
print("Array Multiplication (1-D):", arr_multiplication) 
    
# 2-D array 
arr2_addition = array_2d + array_2d 
arr2_subtraction = array_2d - array_2d 
arr2_multiplication = array_2d * array_2d 
print("Array Addition (2-D):\n", arr2_addition) 
print("Array Subtraction (2-D):\n", arr2_subtraction) 
print("Array Multiplication (2-D):\n", arr2_multiplication)





# ####2.2
# import numpy as np

# def subtract_1d_array(arr1, arr2):
#     result = arr1 - arr2
#     return result

# def subtract_2d_array(arr1, arr2):
#     result = arr1 - arr2
#     return result

# # Subtraction on 1-D arrays
# array_1d_1 = np.array([1, 2, 3, 4, 5])
# array_1d_2 = np.array([5, 4, 3, 2, 1])
# subtraction_result_1d = subtract_1d_array(array_1d_1, array_1d_2)
# print("1-D Array Subtraction Result:")
# print(subtraction_result_1d)

# # Subtraction on 2-D arrays
# array_2d_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# array_2d_2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
# subtraction_result_2d = subtract_2d_array(array_2d_1, array_2d_2)
# print("\n2-D Array Subtraction Result:")
# print(subtraction_result_2d)




# ###2.3
# import numpy as np

# def main():
#     # 1-D array multiplication
#     arr1d = np.array([1, 2, 3, 4, 5])
#     scalar = 2
#     arr1d_result = arr1d * scalar
#     print("1-D Array Multiplication:")
#     print("Original Array:", arr1d)
#     print("Scalar:", scalar)
#     print("Result:", arr1d_result)
#     print()

#     # 2-D array multiplication
#     arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#     matrix = np.array([[2, 0, 1], [1, 2, 3], [0, 1, 2]])
#     arr2d_result = np.dot(arr2d, matrix)
#     print("2-D Array Multiplication:")
#     print("Original Array:")
#     print(arr2d)
#     print("Matrix:")
#     print(matrix)
#     print("Result:")
#     print(arr2d_result)

# if __name__ == "__main__":
#     main()


