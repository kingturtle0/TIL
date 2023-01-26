'''
조건문
반복문
함수
map 
'''

# a = int(input())
# if a > 5:
#     print("오삼")
# elif a > 3:
#     print("불고기")
# elif a > 4 or a == -1:
#     print("재시도")
# else:
#     print("오삼불고기")

# 숫자 2개 입력받은 후
# 둘 중 큰 수를 출력해 주세요~

# num_1, num_2 = map(int, input().split())
# if num_1 > num_2:
#     print(num_1)
# elif num_1 == num_2:
#     print("두 수는 같습니다.")
# else:
#     print(num_2)
# result = num_1 if num_1 > num_2 else num_2 # 조건표현식
# print(result)

# 1 ~ 100 까지 for문으로 출력
# for num in range(1, 101):
#     print(num, end = " ")

# while문으로도 1 ~ 100까지 출력하기
# num = 1
# while num < 101:
#     print(num, end = " ")
#     num += 1

# 리스트 출력 for 이용하여 출력하기
# lst = [[1,2,3], [4,5,6]]
# print(lst[0][1])
# for i in range(2):
#     for j in range(3):
#         print(lst[i][j], end = " ")

# 1차원 리스트
# 빈 리스트 하나 만든 후 lst의 값에 제곱한 값으로 채우기
# 새로 만들어진 리스트를 출력하기
# lst = [[1,2,3], [4,5,6]]
# multi = []
# for i in range(2):
#     for j in range(3):
#         multi.append(lst[i][j] ** 2)
# print(*multi)
# for i in multi:
#     print(i, end = " ")

# 제곱근을 2차원 리스트에 담아보기
# multi를 2차원 리스트로 만들것임
# lst = [[1,2,3], [4,5,6]]
# multi = [[], []]
# for i in range(2):
#     for j in range(3):
#         multi[i].append(lst[i][j] ** 2)
# print(multi)
# multi = []
# for i in range(2):
#     temp = []
#     for j in range(3):
#         temp.append(lst[i][j] ** 2)
#     multi.append(temp)
# print(multi)

# 딕셔너리
# di = {"kevin":1, "john":2, "bob":3}
# print(di)
# for i in di:
#     print(i, di[i])
# for i, j in di.items():
#     print(i, j)
# print(di.items(), di.keys(), di.values())

# break 반복문을 중간에 멈추고 싶을 때 for while (함수종료가 아님!)
# return 함수의 값을 반환하거나 또는 함수 종료시킬 때 
# lst = [10,20,30,40,50,60,70]
# for i in lst:
#     print(i, end = " ")
#     if i == 50:
#         break
# lst = [[1,2,3],[1,2,3],[1,2,3]]
# flag = 0
# for i in range(3):
#     for j in range(4): 
#         if lst[i][j] == 3:
#             flag = 1
#             break
#         print(lst[i][j], end = " ")
#     if flag:
#         break

# lst = [1,2,3,4,5,6,7]
# continue 반복문 맨 위로 다시 올라감(continue 아래 코드는 실행 안함)
# for i in lst:
#     if i == 5:
#         continue
#     print(i, end = " ")

# lst = [[1,2,3],[1,2,3],[1,2,3]]
# for i in range(3):
#     for j in range(3):
#         if lst[i][j] == 3:
#             continue
#         print(lst[i][j], end = ' ')

# 함수 !!
# lst = [6, 6, 9, 8]
# print(len(lst))
# print(sum(lst))
# print(max(lst))
# print(sorted(lst))

# a = 'A'
# print(ord(a)) # ascii code value

# a = '2' 를 정수 2로 바꾼 후 10을 더한 값을 출력해 주세요.
# a = '2'
# print(int(a) + 10)
# print(ord(a) - ord('0') + 10)

# a = -3
# print(abs(a)) # 절대값
# print(id(a)) # 주소값
# print(pow(3,2)) # 제곱

# import random
# a = [1,2,3,4,5,6]
# print(random.sample(a, 2))

# 사용자 함수 (직접 만든 함수)
# def rabbit():
#     print("rabbit")
# for i in range(3):
#     rabbit()

# 두 숫자를 전달받고 합을 돌려주는 (반환하는) 함수를 만들자.
# def getsum(a, b): # parameter 매개변수
#     return a + b
# print(getsum(3, 4)) # argument 인자값
# a = 3
# b = 7
# ret = getsum(5, 6)
# print(ret)

# 값 2개 반환(튜플)
# def getsum(a, b):
#     return a+b, a*b 
# ret = getsum(5, 6)
# print(ret)
# print(type(ret))

# 값 2개 반환 (전역변수 이용)
# gop1 = 0
# def getsum2(a,b):
#     global gop1
#     gop1 = a * b
#     return a + b
# ret = getsum2(5, 6)
# print(ret, gop1)

# def getsum(a, b = 6, c = 7): # default parameter는 항상 우측에 적기
#     return a + b + c
# ret = getsum(4)
# print(ret)

# 패킹 : 값들을 묶어서 하나의 변수로 할당하는 것
# num = [1,2,3,4,5]
# num2 = (1,2,3,4,5)
# print(num, num2)

# unpacking 
# a,b,c,d,e = num
# print(a,b,c,d,e)
# a,b,c,d,e = num2
# print(a,b,c,d,e)
# 언패킹시 남는 값을 *(asterisk 아스트리스크, 아스트랄) 사용하여 리스트에 담을 수 있다.
# a, b, *c = num
# print(a, b, c)
# print(c)
# a, b, *c = num2
# print(a, b, c)

# def getsum(*a): # 매개변수에 *을 사용하면 리스트가 아닌 튜플이 된다. 가변인자라고 표현한다.
#     sum = 0
#     print(a) 
#     for i in a:
#         sum += i
#     return sum
# result = getsum(1,2,3)
# print(result)

# def print_info(**args):
#     print(args)
#     for i, j in args.items():
#         print(i, j)
# print_info(kevin=1, john=2, bob=3)

# def print_info2(**args):
#     print(args)
#     for i, j in args.items():
#         print(i, j)
# di = {'kate':1, 'amy':2, 'oh':3}
# print_info2(**di)

# map
# 리스트나 튜플같은 순회가능한 데이터 구조 값들에 함수를 일괄적으로 적용
# 적용 후 값을 map이라는 객체로 반환
# 사용법 map(함수, iterables)

# num = ['1','2','3']
# lst1 = []
# for i in num:
#     lst1.append(int(i))
# print(lst1)

# lst2 = map(int, num)
# print(lst2) # map이라는 객체 반환
# print(list(lst2)) # 리스트 형태로 바꿔서 출력
 
# lst1= [1,2,3]
# lst2 = [4,5,6]
# # lst3라는 리스트에 lst1과 lst2의 합을 저장하는 리스트로 만든 후 출력
# def func(a, b):
#     return a + b
# lst3 = list(map(func, lst1, lst2))
# print(lst3)
