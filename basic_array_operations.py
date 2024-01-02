
# # Example 1
# import numpy as np
# arr=np.array([[1,2],[3,4],[4,7]])
# #             example
# #             1, 2
# #             3, 4
# #             4, 7
# #          ___________
# # sum of      8, 13
# print(arr.sum(axis=0))




# import numpy as np
# # arr = [1,23,48,4,7]
# # print(arr[-1:])

# arr2= np.array([[1,23,48],[4,7,7],[3,6,8]])
# print(arr2[0:2,1])
# print("get 2nd and 3rd value")
# print(arr2[:,1:3])


# import numpy as np

# a = np.array([[1,2], [3,4],[6,7]])

# b = np.array([[7,9], [3,8],[5,7]])



#     

# print(np.vstack((a,b)))
# # output
# # [[1 2]
# #  [3 4]
# #  [6 7]
# #  [7 9]
# #  [3 8]
# #  [5 7]]
# print(np.hstack((a,b)))
# # output
# # [[1 2 7 9]
# #  [3 4 3 8]
# #  [6 7 5 7]]

# print(np.arange(30).reshape(2,15))
# # output
# # [[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
# #  [15 16 17 18 19 20 21 22 23 24 25 26 27 28 29]]