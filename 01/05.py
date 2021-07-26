import numpy as np

#  시간표시
print('#  시간표시')

h = np.datetime64('2021-07-26 12')
print(h.dtype)

m = np.datetime64('2021-07-26 12:34')
print(m.dtype)

s = np.datetime64('2021-07-26 12:34:12')
print(s.dtype)
print('--------------------------------')

#  문제1
print('문제1')
day1 = np.datetime64('2021-07-26 12:00:00')
day2 = np.datetime64('2021-07-27 12:00:00')
print(day2 - day1)
# 표시하고 싶은 시간값만 남기고 지우면 단위는 저절로 바뀜
print('--------------------------------')

#  문제2
print('문제2')
day3 = np.datetime64('2021-06-21 12:00:00')
day4 = np.datetime64('2021-07-26 12:30:00')
result = day4 - day3
print(result)
print('--------------------------------')

#  insert
print('#  insert')
arr1 = np.arange(1, 11)
print(arr1.dtype)
print(arr1)
print("arr1 shape = ", arr1.shape)

arr1_insert = np.insert(arr1, 0, 20)
print(arr1_insert)
print("arr1_insert shape = ", arr1_insert.shape)
print()

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
print()

# arr2_insert = np.insert(arr2, 2, 100, axis=1)  # axis 를 0일 경우 행, 1이면 열
arr2_insert = np.insert(arr2, 2, range(10, 12), axis=1)  # 행과 열이 size 가 맞아야 오류가 안 뜸
print(arr2_insert)
print('--------------------------------')

#  3차원으로 표시
print('#  3차원으로 표시')
arr3 = np.arange(27)
arr4 = arr3.reshape(3, 3, 3)
print(arr4)
print()

#  행으로 넣기
print('#  행으로 넣기')
arr4_insert1 = np.insert(arr4, 2, 100, axis=0)
print(arr4_insert1)
print()

#  열로 넣기
print('#  열로 넣기')
arr4_insert2 = np.insert(arr4, 2, 100, axis=1)
print(arr4_insert2)


