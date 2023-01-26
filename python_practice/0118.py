# def func():
#     a = 20
#     print('local', a) # local 20

# func()
# print('global', a) # NameError: name 'a' is not defined

# print(sum) # <built-in function sum>
# print(sum(range(2))) # 1
# sum = 5
# print(sum) # 5
# print(sum(range(2))) # TypeError: 'int' object is not callable

# a = 0
# b = 1
# def enclosed():
#     a = 10
#     c = 3
#     def local(c):
#         print(a, b, c)
#     local(300)
#     print(a, b, c)
# enclosed()
# print(a, b)

# 함수 내부에서 글로벌 변수 변경하기
# a = 10
# def func1():
#     global a
#     a = 3
# print(a) # 10
# func1()
# print(a) # 3

# nonlocal 예시
# x = 0
# def func1():
#     x = 1
#     def func2():
#         nonlocal x
#         x = 2
#     func2()
#     print(x) # 2 

# func1() 
# print(x) # 0

# 선언된 적 없는 변수의 활용 nonlocal, global 활용
# def func1():
#     global out
#     out = 3
# func1()
# print(out) # 3

# def func2():
#     def func3():
#         nonlocal y
#         y = 2
#     func2()
#     print(y)
# func2() # SyntaxError: no binding for nonlocal 'y' found

'''
filter
lambda
문자열
'''

# filter
# 리스트나 튜플과 같은 순회가능한 데이터 구조 값들을 함수에 적용하는데
# 적용 후 리턴되는 값 중 True만 반환 (filter라는 객체로 반환)

# 리스트에서 짝수만
# num = [1,2,3,4,5,6]
# def get_even(t):
#     return True if t%2==0 else False
# result = filter(get_even, num)
# print(list(result))

# lambda
# 익명함수 함수를 간략하게 적기 위해서 사용

# 숫자 2개 입력받고 getsum함수로 전달
# get sum 함수에서 전달받은 두 수의 합을 리턴
# def getsum(a,b):
#     return a+b
# ret = getsum(3,5)
# print(ret)
# result = (lambda a,b:a+b)(3,5)
# print(result)
# sum2 = (lambda a,b:a+b)
# print(sum2(3,5))

# 두 리스트 값들의 합을 lst3에
# 람다 함수로 값을 채운 후 출력하기
# lst1= [1,2,3,4,5]
# lst2= [6,7,8,9,10]
# sumlist = (lambda x,y:x+y)
# lst3 = list(map(sumlist, lst1, lst2))
# print(lst3)

# lst3 = list(map((lambda x,y:x+y), lst1, lst2))
# print(lst3)

# 리스트에서 짝수만 빼오기
# lst = list(range(1,100))
# lst2 = filter((lambda even: even%2==0), lst)
# print(list(lst2))

# 데이터에 일괄적용 = map
# 데이터에 일괄적용하는데 True값만 따로 저장하겠다 = filter
# lambda 익명함수 (사용자 함수를 직접 적지 않고 간단하게 함수 사용하고 싶을 때 사용)

# recursion 재귀, 재귀호출
#1 2 3 4 5 6 7 8 9 10 10 9 8 7 6 5 4 3 2 1
# for i in range(1, 11):
#     print(i, end = ' ')
# for i in range(10, 0, -1):
#     print(i, end = ' ')

# def abc(level):
#     if level == 4:
#         return
#     print(level, end = ' ')
#     abc(level + 1)
#     print(level, end = ' ')
# abc(1)

'''
문자열
리스트 튜플 딕셔너리 셋 관련 메소드
copy (깊은복사 얕은복사)
'''

# 문자 'a'가 존재하는지 확인하고자 합니다.
# st = 'apple,banana,mango'
# idx = st.find('a', 1) # 없으면 -1값 반환 뒤의 인자는 찾기 시작하는 위치값
# print(idx)
# alpha = st.index('p') # 없으면 버그
# print(alpha)

# 대소문자 확인
# st = 'apple,banana,mango'
# print(st.isupper())
# print(st.islower())
# print(st.isalpha())
# print(st.count('a')) # 문자열에서 문자의 개수

# join (합치기)
# st = ['a', 'p', 'p', 'l', 'e']
# str2 = "".join(st) # "" 안에는 구분자를 넣습니다
# print(str2) # apple
# 리스트안에 문자를 합치는데 사이사이에 ,를 넣어라
# str3 = ",".join(st)
# print(str3) #a,p,p,l,e
# st = ['apple', 'banana', 'mango']
# str4 = "\n".join(st)
# print(str4)

# 모두 대문자 or 소문자로 바꾸기
# st = 'apple,banana,mango'
# str5 = st.upper()
# print(str5)
# str6 = str5.lower()
# print(str6)

# 공백지우기
# st = '  apple'
# print(st)
# str7 = st.lstrip()
# print(str7)
# st = '  apple     '
# str8 = st.strip() # 양쪽 공백 다 지우기
# print(str8)

# 교체 replace
# st = 'apple'
# str9 = st.replace('ap', 'mp')
# print(str9)

# 리스트 값 추가
# st = ['apple', 'banana', 'mango']
# st.append('orange')
# st.insert(1, 'orange') # 리스트 값을 중간 또는 맨 앞에 추가할 때 사용
# print(st)

# st = [1,2,3]
# st2 = [4,5]
# st.append(st2) # 리스트가 들어간다
# print(st)
# st = [1,2,3]
# st2 = [4,5]
# st.extend(st2) # 값만 추가
# print(st)
# st = [1,2,3]
# st2 = [4,5]
# st += st2 # extend와 같다
# print(st)

# 리스트 값 지우기
# st = [1,2,3]
# st.pop() # 가장 뒤 없앰
# print(st)
# st=[1,2,3,4,1,2,3,4]
# st.remove(4) # 제일 앞에서부터 가장 먼저 찾는 하나만 
# print(st)
# st=[1,2,3,4,1,2,3,4]
# del st[3:]
# print(st)
# st=[1,2,3,4,1,2,3,4]
# st.reverse() # 원본데이터를 뒤집음
# print(st)
# print(st[::-1]) # 뒤집어서 출력만

# sort
# a1 = [6,3,9]
# print(a1)
# a1.sort() # 오름차순이 default
# print(a1)
# a1.sort(reverse=True) # 내림차순
# print(a1)

# a1 = [6,3,9]
# ret = sorted(a1) # 원본 데이터 값 유지(sort랑 다른점)
# print(a1, ret)
# ret = sorted(a1, reverse=True)
# print(a1, ret)

# lambda를 이용한 sort
# lst = list(range(10))
# print(lst)
# ret = sorted(lst,key=lambda x:x) # ret = sorted(lst) 랑 같음 key는 어떻게 sort할것인지
# ret = sorted(lst,key=lambda x:x, reverse=True) # 문자나 숫자나 다 내림차순으로 작동
# ret = sorted(lst,key=lambda x:-x) # 내림차순이지만 숫자만 가능 문자는 정렬 안됨!

# last = 'ergjnjdkngjk'
# ret = sorted(last, key = lambda x:x, reverse = True)
# print(ret)
# ret = sorted(last, key = lambda x:-x) # TypeError
# print(ret)


# lst = [(3,'banana'), (2,'apple'), (1,'carrot')] 
# ret = sorted(lst, key = lambda x:x[1]) # 문자를 기준으로 오름차순 sort하겠다
# print(ret)

# 딕셔너리
# st = {'kevin':1, 'john':2, 'bob':3}
# 딕셔너리 (key랑 value 추가하기)
# st['kate'] = 'hi'
# print(st)
# st['kevin'] = 11
# print(st)
# del st['kate']
# print(st)

# lst = st.keys()
# print(lst)
# print(list(lst))
# lst = st.values()
# print(lst)
# print(list(lst))
# lst = st.items()
# print(lst)
# print(list(lst))
# ret = sorted(lst, key = lambda x:x[1])
# print(ret)

# 딕셔너리 값 출력하기
# st = {'kevin':1, 'john':2, 'bob':[1,2,3]}
# print(st['keein']) # 잘못쓰면 버그
# print(st.get('keein', '값 없음')) # 잘못 쓰면 None을 리턴 => 웬만하면 get 쓰자 (뒤의 인자는 없는 키에 대한 반환 값 None대신 지정가능)

# 딕셔너리 값 정렬하기
# st = {'kevin':27, 'john':22, 'bob':35}
# # 나이가 적은 순으로 (오름차순) 딕셔너리를 정렬하기
# ret = dict(sorted(st.items(), key = lambda x: x[1])) # 많이 쓰진 않음 하지만 정렬 가능하다~
# print(ret)

# a = 5
# b = a  # 주소를 가리킴
# print(b)
# a = 3
# lst = [1,2,3]
# lst2 = lst
# lst[0] = 100
# print(*lst2) # lst2를 바꾸지 않았지만 저장된 주소를 가리키기 때문에 100출력

# lst = [1,2,3]
# lst2 = lst.copy() # 얕은복사 copy랑 [:]는 내부적으로 같은
# lst[0] = 100
# print(lst2)
# lst2 = lst[:] # 얕은복사
# lst[0] = 100
# print(lst2)

# lst = [[1,2],[3,4]] # 전체 리스트가 주소를 참조, 안의 리스트들도 각각의 주소를 참조
# lst2 = lst[:] # copy() 얕은 복사 이후
# lst[0][0] = 10
# print(lst2) # 2차원 배열은 문제가 생긴다 => 깊은 복사를 하자

# 깊은 복사
# import copy # copy모듈의 deepcopy 사용
# lst = [[1,2],[3,4]]
# print(id(lst), id(lst[0]), id(lst[1]))
# lst2 = copy.deepcopy(lst)
# print(id(lst2), id(lst2[0]), id(lst2[1]))
# lst[0][0] = 10
# print(lst2)

# 주소값을 찍어보자
# a = 5
# b = 5
# print(id(a), id(b)) # 주소 같음
# lst = [1,2,3]
# lst2 = lst
# print(id(lst), id(lst2)) # 주소 같음
# 리스트 얕은 복사
# lst = [1,2,3]
# lst2 = lst[:]
# print(id(lst), id(lst2)) # 주소 다름
# 2차원 배열 얕은 복사
# lst = [[1,2],[3,4]]
# lst2 = lst[:]
# print(id(lst), id(lst2)) # 주소 다름
# print(id(lst[0]),id(lst2[0])) # 주소 같음
# 깊은복사
# import copy
# lst = [[1,2],[3,4]]
# lst2 = copy.deepcopy(lst)
# print(id(lst), id(lst2)) # 주소 다름
# print(id(lst[0]),id(lst2[0])) # 주소 다름