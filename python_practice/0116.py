# 변수
# a = 3
# b = 5

# print(f"{a} + {b} = {a + b} 입니다")

# swap
# a = 3
# b = 5

# temp = a
# a = b
# b = temp
# a, b = b, a
# print(a, b)

# 자료형
# a = 3
# print(type(a))
# a = 3.14
# print(type(a))
# print(round(a, 1)) # 소수점 첫번째 까지만 출력
# print(f"{a:.1f}")

# a = 5
# a = str(a)
# print(a)
# print(type(a))

# 오늘은 "100%" 입니다
# print('오늘은 "100%" \n 입니다')

# slicing

# s = "abcdefg"
# print(s[:3]) # 3번원소(인덱스) 직전까지: abc
# print(s[3:]) # defg
# print(s[2:5]) # cde
# print(s[5:2:-1]) # 5 4 3 fed
# print(s[1:5:2]) # 1 3 bd

# boolean
# a, b = 0, -1
# a, b = bool(a), bool(b)
# print(a, b)

# list
# lst = [1, 2, 3, 4, 5]
# print(lst)
# print(*lst)
# print(type(lst))

# print(lst[1]) # 2
# print(len(lst)) # 리스트의 길이 5
# print(lst[-1])

# tuple
# tp = (1, 2, 3, 4, 5)
# print(tp)
# print(*tp)
# print(type(tp))
# print(len(tp))
# print(tp[-1])

# range
# print(list(range(3))) # 0 1 2
# print(list(range(1, 5))) # 1 2 3 4

# set - 리스트에서 중복된 것 제거할 때 많이 사용
# lst = [2, 2, 2, 3, 5, 6, 6]
# lst = list(set(lst))
# print(lst)

# 논리 연산자의 단축 평가
# 결과가 확실한 경우 두 번째 값은 확인하지 않고 첫번째 값 반환
# and 연산에서 첫번째 값이 False인 경우 무조건 False => 첫번째 값 반환
# or 연산에서 첫번째 값이 True인 경우 무조건 True => 첫번째 값 반환
# print(3 and 5)
# print(3 and 0)
# print(0 and 3)
# print(0 and 0)

# print(5 or 3)
# print(3 or 0)
# print(0 or 3)
# print(0 or 0)

# set (중복을 허용하지 않는 데이터들의 묶음)

# # 값 추가
# s = {1, 2, 3, 4, 5}
# s.add(6) # 1개 추가
# print(s) 
# s.update([11, 12, 8, 7, 6]) # 여러개 추가
# print(s)

# # 값 삭제
# s.remove(6) # 삭제하는 값이 없으면 버그남!!
# print(s)
# s.discard(12) # discard는 값이 없어도 버그 안남
# print(s)
# s.clear() # 다 삭제
# print(s)

# 집합
s1 = [1, 2, 3, 4, 5]
s2 = [2, 4, 6, 8]

# 교집합
s1, s2 = set(s1), set(s2)
print(s1 & s2)

# 합집합
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)