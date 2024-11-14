# 집합 자료형
# 중복된 요소는 제거되고 반환됨
# 순서가 없음
# 다시 리스트나 튜플로 바꿔서 자료를 쓴다
# 교집합, 합집합, 차집합 가능
# 다 필요없고 중복되는 값 제거에 사용함. set에 넣었다가 다시 list를 만들면 중복제거 됨

####  set 자료형은 주로 리스트의 요소들 중복 제거 하는 용도로 사용
## set()  문자열, 튜플, 리스트 를 넣을 수 있다 literal
list2 = [100, 200, 100, 100, 300, 200, 200, 300]
set2 = set(list2)
print(set2)

set1 = set([10, 20, 30])
print(set1)  # {10, 20, 30}

set2 = set("Korea")
print(set2)  # {'a', 'K', 'r', 'e', 'o'} 문자열은 실행 할 때 마다 순서가 바뀜

set3 = set([10, 20, 10, 10, 30, 20, 20, 30])
print(set3)  # {10, 20, 30} 중복된 요소는 한개로 표현됨

# 중복이 제거된 값만으로 리스트를 만듬
list1 = list(set3)
print(list1)

## bool 참고
## True, False
a = True
if 10>5:
    print("10은 5보다 크다")

print(10>5)

bool("")  # 아무것도 없는 문자열 false, 공백이라도 입력되면 True. [] {} () 다 거짓임
bool(None)  # false
print(bool(10))  ## bool 연산 0을 제외한 모든 숫자는 True

# swqp 참고 그다지 쓸일은 없다
a = 10   # b= 10 a = 20 으로 변경
b = 20

a, b = b, a
print(a, b)