# EXAMPLE 1

# import numpy as np
# arr = np.array([1,2,3,4,5,6])

# print(arr[0])
# print(arr)



# EXAMPLE 2
# import numpy as np
# import time
# import sys

# l = range(1000)

# print(sys.getsizeof(5) * len(l))

# array = np.arange(1000)
# print(array.size * array.itemsize)


# EXAMPLE 3
# import numpy as np
# import time
# import sys


# SIZE = 1000
# l1 = range(SIZE)
# l2 = range(SIZE)

# a1 = np.arange(SIZE)
# a2 = np.arange(SIZE)


# # python list
# start = time.time()
# result = [(x+y) for (x,y) in zip(l1,l2)]
# print("python list took : ", (time.time() - start)*1000)


# # Numpy List
# start = time.time()
# result = a1 + a2
# print("Numpy took : ", (time.time() - start)*1000)




# EXAMPLE 4
# import numpy as np
# a1 = np.array([1,2,3,4,5,9])
# a2 = np.array([1,2,3,4,5,3])

# result = a1+a2
# result2 = a1-a2
# result3 = a1*a2
# result4 = a1/a2
# print(result)
# print(result2)
# print(result3)
# print(result4)



# EXAMPLE 5
# import numpy as np
# a1 = np.array([[1,2,4],[3,4,5],[5,9,6]])
# print(a1.ndim)
# print(a1.itemsize)
# print(a1.dtype)
# a1 = np.array([[1,2,4],[3,4,5],[5,9,6],[5,9,6]],dtype=np.float64)
# print(a1.itemsize)
# print(a1.size)
# print(a1.shape)
# a1 = np.array([[1,2,4],[3,4,5],[5,9,6],[5,9,6]],dtype=complex)
# print(a1)


# EXAMPLE 6
# import numpy as np
# array = np.zeros((2,3))
# print(array)

# array = np.ones((2,3))
# print(array)



# EXAMPLE 6
# import numpy as np

# l=range(5)
# print(l)
# l=np.arange(1,5)
# print(l)
# l=np.arange(1,53,3)
# print(l)
# l=np.linspace(1,5,20)
# print(l)
