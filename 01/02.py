import numpy as np


#  arange
print('#  arange 1')

arr1 = np.arange(64)
print(arr1)
print('--------------------------------')

#  reshape : 2차원 배열로 바꿔줌
print('#  reshape 2')

arr2 = arr1.reshape(4, 16)
print(arr2)
print('--------------------------------')

#  reshape : 3차원 배열로 바꿔줌
print('#  reshape 3')

arr3 = arr1.reshape(4, 4, 4)
print(arr3)
print('--------------------------------')
