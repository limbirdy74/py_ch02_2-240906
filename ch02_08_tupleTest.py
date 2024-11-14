# 튜플은 초기에 선언된 값을 변경 할 수 없다
# 원본의 내용을 수정할 수 없다.
# 프로그램이 종료될 까지 유지할 값을 튜플을 이용한다

tuple1 = (10, 20, 30, 40)
print(tuple1[2])  # index는 [] 을 쓴다
print(len(tuple1))
tuple1 = tuple1 + tuple1
print(tuple1)
print(tuple1.count(10))  # 튜플에 쓸 수 있는 두가지 함수, 해당 값의 빈도수
print(tuple1.index(10))  # 해당값의 처음 인덱스

#  리스트 튜플을 상호 변환 할 수 있다
list1 = list(tuple1)
print(list1)

list2 = [10, 20, 30]
tuple2 = tuple(list2)
print(tuple2)

# 참고 데이터 타입 변환
num1 = 100
numstr1  = "200"

print(num1 * numstr1)   #  200이 100번 찍힘
# print(num1 + numstr1)   #  오류남
print(num1 + int(numstr1))  #  숫자형 자료형 변경 300 반환. 원본이 바뀌진 않고 임시직 형변환
# 100200 출력
print(str(num1) + numstr1)  #  문자형 자료형 변경.