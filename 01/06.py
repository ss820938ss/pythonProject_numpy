import numpy as np

#  배열 값 수정하기
print('#  배열 값 수정하기')
arr1 = np.arange(1, 11)
print(arr1)

arr1[0] = 100
print(arr1)

arr1[:5] = 100
print(arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2[0, :3] = 0  # 첫번째는 항상 행, 두번째는 열
print(arr2)
print('--------------------------------')

#  배열 값 삭제
print('#  배열 값 삭제')
arr3 = np.arange(10)
print(arr3)

arr3_delete = np.delete(arr3, 0)
print(arr3_delete)
print('--------------------------------')

#  행과 열을 지우기
print('#  행과 열을 지우기')
arr4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr4)
arr4_delete_row = np.delete(arr4, 2, axis=0)  # 행
print(arr4_delete_row)
arr4_delete_attr = np.delete(arr4, 2, axis=1)  # 열
print(arr4_delete_attr)
print('--------------------------------')

#  연습
print('#  연습')

arr5 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr5)
arr5_delete_row = np.delete(arr5, 2, axis=0)
print(arr5_delete_row)
arr5_delete_attr = np.delete(arr5, 2, axis=1)
print(arr5_delete_attr)
print()

arr6 = np.arange(27)
arr6_2 = arr6.reshape(3, 3, 3)
print(arr6_2)

arr6_delete_row = np.delete(arr6, 2, axis=0)
print(arr6_delete_row)
#  이거 왜 range 는 그 숫자밖에 안지워지지
print('--------------------------------')

#  배열의 데이터타입 변환
print('#  배열의 데이터타입 변환')

arr7 = np.array(['1.5', '2', '2.7', '4'])
# arr7 = np.array([1, 2, 3, 4])
print(arr7)
print(arr7.dtype)

change_arr7 = arr7.astype(float)
print(change_arr7)
print(change_arr7.dtype)

change_int = change_arr7.astype(int)
print(change_int)
print(change_int.dtype)
print('--------------------------------')

#  연습
print('#  연습')
arr8 = np.array([1, 2, 3, 4])
print(arr8)
print(arr8.dtype)

change_arr8 = arr8.astype(int)
print(change_arr8)
print(change_arr8.dtype)

change_arr8_float = change_arr8.astype(float)
print(change_arr8_float)
print(change_arr8_float.dtype)

change_arr8_str = change_arr8.astype(str)
print(change_arr8_str)
print(change_arr8_str.dtype)
print('--------------------------------')

#  배열의 연산
print('#  배열의 연산')

arr9 = np.arange(1, 11)
print(arr9)
arr10 = np.arange(101, 111)
print(arr10)
print()

result = arr9 + arr10
print('더해진 값 >> ', result)
print()

print(arr9 * 2)
print(arr9 ** 2)
print((arr9 ** 2)/arr10)
print()

arr11 = np.arange(1, 11)
print(arr11.sum())
arr12 = np.arange(1, 1001)
print(arr12.sum())

print(arr11.mean())
print(arr11[0] > 3)
print()

#  값과 값의 비교
print('#  값과 값의 비교')
arr13 = np.arange(1, 11)
arr14 = np.arange(100, 111)
print(arr13[0])
print(arr14[0])
print(arr13[0] < arr14[0])
