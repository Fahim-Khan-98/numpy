# # Example 1

# import numpy as np

# a = np.arange(15).reshape( 5,3)

# print("array : ",a)
# print("===")
# aw=0

# for row in a:
#   print(row)
# print("===")
# for row in a:
#   for cell in row:
#     print("Element:", cell)
#     aw += cell
# print("===")
# print("Cumulative Sum:", aw)




# Shorter of example 1 
# i also print cell using flat

# import numpy as np

# a = np.arange(15).reshape( 5,3)
# for cell in a.flat:
#   print(cell)


# Example 2  
# C order
# import numpy as np
# a = np.arange(15).reshape( 5,3)

# for x in np.nditer(a, order="C"):
#   print(x)


# Fortan order
# import numpy as np
# a = np.arange(15).reshape( 5,3)

# for x in np.nditer(a, order="F"):
#   print(x)