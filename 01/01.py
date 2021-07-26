import numpy as np

#  배열생성
print('#  배열생성')

#  1차원
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
print(arr1[2])
print(arr1[2], arr1[4])

data = [11, 22, 33, 44]
arr2 = np.array(data)
print(arr2)

arr1[0] = 100
print(arr1)


#  2차원
arr3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr3)

zeroToZero = arr3[0, 0]
a = arr3[2, 1]
print(zeroToZero, a)


#  3차원
arr4 = np.array([
                [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [[10, 20, 30], [40, 50, 60], [70, 80, 90]],
                [[100, 200, 300], [400, 500, 600], [700, 800, 900]]
                ])
print(arr4)

zero_zero_zero = arr4[0, 0, 0]
b = arr4[2, 1, 0]
print(zero_zero_zero, b)

print()
print('#  9, 50, 700 띄우기')
print(arr4[0, 2, 2])
print(arr4[1, 1, 1])
print(arr4[2, 2, 0])
print('--------------------------------')


#  연습
print('#  연습')
#  1차원
num1 = np.array([1, 2, 3, 4, 5])
print(num1[3])

#  2차원
num2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(num2[2, 1])

#  3차원
num3 = np.array([
                [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [[23, 34, 21], [54, 56, 11], [49, 89, 60]],
                [[243, 432, 390], [943, 547, 738], [923, 443, 503]]
                ])
print(num3[2, 0, 1])
print('--------------------------------')


#  range 사용
print('#  range 사용')
data2 = range(1, 10)
data3 = range(11, 20)
arr5 = np.array([data2])
arr6 = np.array([data3])
print(arr5, arr6)
print('--------------------------------')
