a = 10
b = 20
c = 30
d = 15
e = 45

list1 = [10, 20, 30, 15, 45]  # 리스트 자료구조
list2 = [10, "korea", 3.14]   # 리스트 다양한 자료형 입력 가능
list3 = [10, 20, 30, ["kor", "math", "eng"]]  # list3의 요소는 4개

print(list1)
print(list1[2])  # 인덱싱
print(list1[-2])  # 15 뒤에서 부터 카운팅
print(list1[2:])  # 슬라이싱
print(list1[2] + list1[0])  # 리스트 요서간 연산가능

print(list3[3][1])  # 리스트안에 리스트를 읽어오기 math 반환
print(list3[3][1][2])  # math 의 인덱스 2번 t 가 찍힘, 문자열도 하나의 list
#list2 korea 알파벳 r을 찍기
print(list2[1][2])

# 리스트 연산
list5 = [1,2,3]
list6 = [4,5,6]
list7 = list5 + list6  # 리스트가 합쳐짐 [1, 2, 3, 4, 5, 6]
print(list7)

print(list5 * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

print(len(list7))  # 6 을 반환. 리스트의 총 길이를 파악할 때 사용

# 리스트 요소 값 수정
list8 = [50, 30, 20, 100, 90]
list8[2] = 80
print(list8)

# 리스트 특정 요소 삭제
del list8[3]   # 인덱스 값으로 삭제
print(list8)

del list8[1:3]  # 인덱스 1 ~ 2를 삭제해라. 슬라이싱 됨
print(list8)
