# import numpy as np 
# import time 
# l1=[1,2,3]
# l2=[6,7,8]
# list(zip(l1,l2))

# # size=1,00,000
# # l1=list(range(size))
# # l2=list(range(size))


# start=time.time()
# # add=[x+y for x,y in zip(l1,l2)] 
# # end=time.time()
# # print(end - start)
# print(start)

import numpy as np
import time

# Python list
size = 1_000_000
list1 = list(range(size))
list2 = list(range(size))

start = time.time()
result = [x + y for x, y in zip(list1, list2)]
end = time.time()
print("Python list addition time:", end - start)

# NumPy array
arr1 = np.array(list1)
arr2 = np.array(list2)

start = time.time()
result = arr1 + arr2  # Vectorized operation
end = time.time()
print("NumPy array addition time:", end - start)