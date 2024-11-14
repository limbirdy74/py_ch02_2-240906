list1 = []  # 빈 리스트 선언 가능
print(list1)

list1.append(10)  # 내장 함수 이용
print(list1)

list1.append(15)  # 기존 리스트에 마지막 요소로 추가됨
print(list1)      # 최종 [10, 15]

list2 = [15, 20, 40]
# list2 중간에 삽입 15 30 20 40 으로 만들기
list2.insert(1, 30)  # (삽입할 인덱스, 삽입 값)
print(list2)

# 리스트 내용 삭제
list3 = [100, 200, 300, 400, 300]
# del list3[2]  # del 로 삭제시는 인덱스사용
# print(list3)
list3.remove(300)  # 지울 값을 넣어준다. 값이 여러개일 경우 첫번째 값만 지운다
print(list3)
list3.remove(300)  # 최종으로 300이 모두 지워짐
print(list3)

# 리스트 정렬 - 오름차순 정렬, 내림차순 정렬
list4 = [100, 15, 7, 30, 65, 90]
list4.sort()  # 리스트 원본의 내용이 변경됨
print(list4) 

list5 = [100, 15, 7, 30, 65, 90]
list5.sort(reverse=True)  # 내림차순으로 정렬 
print(list5)

# list55 = list5.sort()  # 안됨 왜 안될 까
# print(list55)

list6 = ["kor", "math", "eng"]
list6.sort()  # 문자열의 첫글자의 알파벳순으로 정렬
print(list6)

# 많이 쓰지 않음 알아만 두자
list7 = [80, 60, 100]
list7.reverse()  # [100, 60, 80] 정렬순서에 상관없이 순서를 뒤집는다
print(list7)

list8 = [100, 200, 300, 400, 300]
print(list8.index(300))  # 해당 값의 인덱스 반환
# print(list8.index(350))

list9 = [1, 2, 2, 3, 1, 1]
print(list9.count(1))  # 리스트내의 해당 값의 빈도수를 나타낸다

list10 = [10, 20, 30]
print(list10.pop())  # 30 해당 리스트이 마지막 원소를 반환 -> 꺼낸 마지막 요소가 리스트에서 제거됨
print(list10)  # [10, 20] 반환됨

list11 = [10, 20, 30]
print(list11.pop(1))  # 숫자를 써 주면 인덱스
print(list11)  # [10, 30] 반환됨

list12 = [10, 20]
list13 = [30, 40]
list12.extend(list13)  # 리스트에 리스트를 더하는 함수. 값으로 리스트만 가능
print(list12)

list14 = [10, 20]
list15 = [30, 40]
list14 = list14 + list15  # extend 에 와 같은 결과
print(list14)