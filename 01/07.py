import numpy as np
import matplotlib.pyplot as plt

#  NumPy 로 구구단 배열 만들기
print('#  NumPy 로 구구단 배열 만들기')

row = np.arange(2, 10)
attr = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9]])

result = row * attr

print(result)
print(result.T)  # .T 행과 열의 축을 변경
print('--------------------------------')

print(result.sum())
print(result.mean())
print(result.shape)  # result 기본값에 대한 값
print(result.T.shape)  # result.T 에 대한 값
print(result.dtype)
print('--------------------------------')

#  float 값으로 변경
print('#  float 값으로 변경')

result_change = result.astype(float)
print(result_change)
print(result_change.dtype)
print('--------------------------------')

#  float 값으로 변경2
print('#  float 값으로 변경2')

arr1 = [(1, 2, 3), (4, 5, 6)]
print(arr1)
a = np.array(arr1, dtype=float)
print(a)
print(a.dtype)
print('--------------------------------')

#  linspace 의 데이터 추출 시각화
print('#  linspace 의 데이터 추출 시각화')

a = np.linspace(0, 1, 5)
print(a)
print()

# plt.plot(a, 'o')  # 'o' 를 빼면 기본값은 선으로 나옴
# plt.plot(a, '--')  # '--' 는 점선
# plt.hist(a, bins=10)  # 히스토그램, bins 안의 숫자 변경시 바의 크기 변경

plt.show()
print('--------------------------------')

#  a배열 파일에 저장
print('#  a배열 파일에 저장')
# np.save("./data", a)
print('--------------------------------')

#  배열의 차원 수
print('#  배열의 차원 수 ')

arr2 = np.arange(64)
arr3 = arr2.reshape(4, 16)
arr4 = arr2.reshape(4, 4, 4)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)
print('--------------------------------')

#  문제 : 추석까지 몇시 몇분 몇초 남았는지
print('#  문제 : 추석까지 몇시 몇분 몇초 남았는지')

day1 = np.datetime64('2021-07-26 16:38:00')
day2 = np.datetime64('2021-08-15 12:00:00')
result = day2 - day1
print(result)

day1 = np.datetime64('2021-07-26 16:38')
day2 = np.datetime64('2021-08-15 12:00')
result = day2 - day1
print(result)

day1 = np.datetime64('2021-07-26 16')
day2 = np.datetime64('2021-08-15 12')
result = day2 - day1
print(result)
print()

#  문제 : 추석까지 몇시 몇분 몇초 남았는지2
print('#  문제 : 추석까지 몇시 몇분 몇초 남았는지2')

day1 = np.datetime64('2021-07-26 16:38:00')
day2 = np.datetime64('2021-08-15 12:00:00')
result = day2 - day1
print(result)

result_type_change = result.astype(str)
print(result_type_change.dtype)


