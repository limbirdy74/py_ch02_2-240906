# key : value 형식으로 , 로구분 key 값이 중복 될 순 없다
# 딕셔너리는 추가 삭제 가능
dic1 = {"이름":"홍길동", "점수":100, "나이":27, "전화번호":"010-1234-1234"}  # 딕셔너리  key : value 방식

# print(dic1[0])  # 오류남
print(dic1["이름"])
print(dic1["나이"])

dic2 = {1:"야구", 2:"축구", 3:"배구"}
print(dic2[1])
print(dic2[2])

# 새로운 딕셔너리 쌍 추가
dic2[4] = "농구"
print(dic2)

dic2[0] = "농구"  # 값은 중복되어도 상관없고 뒤에 붙는다
print(dic2)

dic1["주소"] = "서울 종로구"
print(dic1)

# 딕셔너리 요소 삭제
del dic2[3]  # key 값으로 삭제함
print(dic2)

# 딕셔너리 요소 수정
dic2[0] = "배구"  # 이미 존재하는 key 값이면 수정됨
print(dic2)

dic2[5] = ["서울", "부산", "인천"]  # value 값은 아무거나 가능(리스트도 가능), key 값으로 리스트는 불가
print(dic2)

dictemp = dic1.values()  # 딕셔너리의 값만 읽어서 리스트로 만들어줌
print(dictemp)
dictemp2 = dic1.keys()  # 딕셔너리의 키만 읽어서 리스트로 만들어
print(dictemp2)
dictemp3 = dic1.items()  # 딕셔너리의 키만 읽어서 리스트로 만들어
print(dictemp3)  # ([('이름', '홍길동'), ('점수', 100), ('나이', 27), ('전화번호', '010-1234-1234'), ('주소', '서울 종로구')])
                 #  튜플구조의 리스트로 만들어 반환, 인덱스로 꺼내 쓸 수 있지만 자료의 변경은 불가능

print("점수" in dic1)  # True 반환, 딕셔너리 내에 key값이 존재하는지 여부

score = dic1.get("점수")  # key 값에 대응되는 value 값 반환
# score = dic1["점수"]
print(score)

# print(dic1["점슈"]) #해당 key 값이 없으므로 오류남
print(dic1.get("점슈"))  # None 값 반환 -> error 발생 안함. None - 다른 언어에선 NULL값
# dic1["점슈"] # 오류남


dic1.clear()  # 딕셔너리 모든 요서 삭제
print(dic1)

#참고
listtemp = []
str = ""
a = None
print(listtemp)
print(str)
print(a)