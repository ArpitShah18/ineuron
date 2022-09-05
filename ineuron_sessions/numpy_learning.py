# Aug 13 2022 session
import numpy as np

l = [1, 2, 3, 4, 5, 6]

op = np.array(l)

# print(op)

l1 = [1, 2, 3, 'sudh', True, 2.55]
# As array stores all elements of same type it will convert all elements in string
op1 = np.array(l1)
# print(op1)

# ['1' '2' '3' 'sudh' 'True' '2.55']

# print(op1.ndim)

l2 = np.array([[1, 2, 3], [4, 5, 6]])
# print(l2)
# 2D array
# [[1 2 3]
#  [4 5 6]]
# print(l2.ndim)
l3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
# print(l3)

# printing dimmension , its 3D array
# print(l3.ndim)
# [[[1 2 3]
#   [4 5 6]
#   [7 8 9]]]

l4 = np.random.randint(2, 5)  # will generate a random number between 2,5
# print(l4)

l5 = np.random.randint(2, 50, (3, 4))  # will generate a random number between 2,50 with 3 rows and 4 columns
# print(l5)
# [[13 42 14  9]
#  [ 4 40 26 17]
#  [ 9 45 47 21]

l6 = np.random.randint(2, 50, (2, 3, 4))  # will generate a random number between 2,50 with 2 matrices having 3 rows
# and 4 columns ie 3D array

# print(l6)

# [[[46 23 31  9]
#   [49 31 20 11]
#   [27 35 35 46]]
#
#  [[49 43 13 37]
#   [24 13 43 34]
#   [16 46 41 22]]]
l7 = np.random.randn(4,4) # will generate 2D array with values which are normally distributed
# means mean = 0 and std deviation = 1
# print(l7)

# [[ 0.39607654 -0.04681066  0.47927602  0.58864952]
#  [-3.12625661 -1.69363307 -1.16365677 -1.1288934 ]
#  [-0.88717771  1.09885781  1.33218648  0.24629192]
#  [ 0.30820002  1.96933209  0.21211238  0.48860434]]

# We can reshape the array with any number of dimmensions but nos should be like that size shouldnt change otherwise
# it will give u value error


l8 = l7.reshape(2,8)
# print(l8)

# [[ 0.40211928 -0.13877045 -0.51787887 -0.07458241 -1.30834546 -0.25810446
#    0.35175671  0.85016025]
#  [ 0.7746813   0.56212154 -1.30804456  0.44424396 -0.11080536 -0.87439638
#   -2.25461271  0.21051828]]

l9 = l7.reshape((2,-2))
# 2nd number will be detected automatically , if we give 2 nd number with any negative value

# print(l9)
# [[ 1.96959014  0.92399999  0.38070286 -1.17797155 -1.21823216 -1.04091287
#    0.51634973  0.52371481]
#  [ 0.79923947  0.02326853  0.22905852 -0.52632907  0.03457447  0.20317121
#   -1.12980451  0.45139677]]

# multipliation of matrices will be done with @ sign ie a6@a7 where a6 and a7 are matrices
# a6 * a7 will do element wise multiplication

