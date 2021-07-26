import numpy as np

#  full
print('#  full')
arr1 = np.full((2, 5), 30)
print(arr1)
print('--------------------------------')

#  nomal
print('#  nomal')
arr2 = np.random.normal(10, 5, (3, 3))
print(arr2)
print('--------------------------------')

#  randint
print('#  randint')
arr3 = np.random.randint(1, 11, (2, 5))
print(arr3)
print()

arr4 = np.random.randint(11, 20, (2, 5))
print(arr4)
print()

print(arr3 + arr4)
print((arr3 + arr4) / 2)
print(arr4 * 2)
print('--------------------------------')

#  날짜
print('#  날짜')
date1 = np.array('2021-07-26')
print(date1)
print(date1.dtype)
print()

date2 = np.array('2021-07-26', dtype=np.datetime64)
print(date2)
print(date2 + 10)  # 날짜 경과
print(date2.dtype)
print()

date3 = np.array('2021-11-11', dtype=np.datetime64)
print(date3)
print(date3.dtype)
print(date3 - date2)  # 남은 날 계산
print('--------------------------------')

#  날짜별 배열
print('#  날짜별 배열')
date4 = np.array('2021-01-01', dtype=np.datetime64)
print(date4)

new_date = date4 + np.arange(30)
print(new_date)  # 해당 데이터 전부 보여줌
print(new_date.shape)  # 해당 데이터 갯수
print(new_date.dtype)  # 해당 데이터 타입
print('--------------------------------')

#  shape 기능
print('#  shape 기능')
arr5 = np.arange(64)
arr6 = arr5.reshape((4, 4, 4))
print(arr6)
print(arr6.shape)
print('--------------------------------')

#  연습
#  shape 와 reshape
print('#  shape 와 reshape')
arr7 = np.arange(27)
print(arr7)
arr8 = arr7.reshape(3, 3, 3)
print(arr8)
print(arr8.shape)
#  reshape 할 때는 총 개수가 맞아야 한다. 즉 size 가 같아야 shape 를 변환할 수 있음.
print('--------------------------------')