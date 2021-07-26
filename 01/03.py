import numpy as np

#  잘못된 예시
print('#  잘못된 예시')
zero = np.array([[0, 0], [0, 0]])
print(zero)
print('--------------------------------')

#  zero 행렬 1차원
print('#  zero 행렬 1차원')
zero1 = np.zeros((5))
print(zero1)
print('--------------------------------')

#  zero 행렬 2차원
print('#  zero 행렬 2차원')
zero2 = np.zeros((5, 5))
print(zero2)
print('--------------------------------')

#  zero 행렬 3차원
print('#  zero 행렬 3차원')
zero3 = np.zeros((5, 5, 5))
print(zero3)
print('--------------------------------')

#  ones : 타입 확인
print('#  ones : 타입 확인')
one = np.ones(5)
print(one.dtype)
print()

#  ones : 1차원
print('#  ones : 1차원')
one1 = np.ones((5))
print(one1)
print()

#  ones : 2차원
print('#  ones : 2차원')
one2 = np.ones((5, 5))
print(one2)
print()

#  ones : 3차원
print('#  ones : 3차원')
one3 = np.ones((5, 5, 5))
print(one3)
print('--------------------------------')

#  단위행렬
print('#  단위행렬')
arr1 = np.array([[1, 2], [3, 4]])
print(arr1)
print()

#  eye
print('#  eye')
unitMatrix = np.eye(2)
print(unitMatrix)
print()

#  arange
print('#  arange')
arr2 = np.arange(1, 30, 3)
print(arr2)
print()

#  linspace
print('#  linspace')
arr3 = np.linspace(1, 100, 5)
print(arr3)
print()

#  0, 1 까지의 숫자가 나오는 랜덤함수
print('#  0, 1 까지의 숫자가 나오는 랜덤함수')
arr4 = np.random.random((3, 3))
print(arr4)
print()

#  정수값이 나오는 랜덤함수
print('#  정수값이 나오는 랜덤함수')
rend_int = np.random.randint(10, 100, (2, 5))  # 10 ~ 100 사이의 숫자를 2, 5 배열로
print(rend_int)
print('--------------------------------')


#  문제1
print('#  문제1')
rent_int2 = np.random.randint(1, 100, (5, 5))
print(rent_int2)
print(rent_int2[2, 2])
print()

#  문제2
print('#  문제2')
rent_int3 = np.random.randint(1, 100, (3, 3, 3))
print(rent_int3)
print(rent_int3[2, 0, 2])

#  문제3
print('#  문제3')
rent_int4 = np.random.randint(1, 100, (3, 3, 3))
print(rent_int4)
print(rent_int4.max())
print(rent_int4.min())  # min, max 사용시 순서 주의
print(rent_int4.mean())
