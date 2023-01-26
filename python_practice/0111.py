# num = 5  # 정수값 5 int(integer)
# print(num)
# print(type(num))
# st='5555'  # 문장 '5555' str(string)
# print(st)
# print(type(st))
# # 자료형 int, str
# # bool = True or False
# boolean = (3>5)
# print(boolean)
# # 문자열 출력 !!!
# name = '오영재'
# age = 29
# # %sting
# # str.format
# # f-string
# # 제 이름은 오영재이고 39살입니다.
# print("제 이름은 %s 이고 %d살 입니다." % (name, age))
# print("제 이름은 {0} 이고 {1}살 입니다.".format(name, age))
# print(f"제 이름은 {name} 이고 {age}살 입니다.")
# # %s 문자열, %d 정수, %f 실수

# lst = [1,2,3,4,5,6,7,8]
# lst = ['Java', 'Django', 'C++', 'Ruby', 'Python']
# print(lst[0])
# print(lst[2])
# print(lst[4])   # 4번 원소 값 출력
# print(len(lst)) # len = 리스트 길이를 알려주는 내장함수
# print(lst[1:4]) # 인덱싱
# # 1. 어제 먹은 아침 점심 저녁 메뉴로 채워진 리스트 하나 만들어보세요.
# menu = ['죽', '갈치조림', '카레']
# # 2. 아침에 먹은 메뉴를 출력해주세요.
# print(menu[0])
# # 3. 저녁에 먹은 메뉴를 출력해주세요.
# print(menu[2])

# 변수
# 리스트
# 딕셔너리 = 다른 언어의 Hash와 동일
# a:b의 a는 key b는 value 라고 한다.

# # 자신의 이름, 나이, 인사말로 구성된 my_info라는 딕셔너리를 하나 만들어주세요.
# my_info = {'name':'YeongjaeOh',
#            'age':'29',
#            'hello':'Nice to meet you!',
#            'study': {'stcamp':'3days',
#                      'python':'2weeks',
#                      'algorithm':'6weeks'},
#            111:'goooooooooood!',
#            999:'so hard:('}
# # my_info 딕셔너리에서 나이만 출력해 주세요.
# # print(my_info['age'])
# # print(my_info['hello'])
# # python 공부 기간을 출력해 주세요.
# print(my_info['study'])
# print(my_info['study']['python'])
# print(my_info[111])
# print(my_info[999])

# movie = {
#     'movieInfo': {
#         'movieNm': '광해, 왕이 된 남자',
#         'movieNmEn': 'Masquerade',
#         'showTm': '131',
#         'prdtYear': '2012',
#         'openDt': '20120913',
#         'typeNm': '장편',
#         'nations': [{'nationNm': '한국'}],
#         'genres': [{'genreNm': '사극'}, {'genreNm': '드라마'}],
#         'directors': [{'peopleNm': '추창민', 'peopleNmEn': 'CHOO Chang-min'}],
#         'actors': [
#             {'peopleNm': '이병헌', 'peopleNmEn': 'LEE Byung-hun', 'cast': '광해/하선'},
#             {'peopleNm': '류승룡', 'peopleNmEn': 'RYU Seung-ryong', 'cast': '허균'},
#             {'peopleNm': '한효주', 'peopleNmEn': 'HAN Hyo-joo', 'cast': '중전'},
#         ],
#     }
# }
# # 1. 영화 제목을 출력해주세요.
# print(movie['movieInfo']['movieNm'])
# # 2. 다음 영화의 감독의 영어 이름을 출력해 주세요.
# print(movie['movieInfo']['directors'][0]['peopleNmEn'])
# # 3. 다음 영화의 배우의 인원을 출력해주세요.
# print(len(movie['movieInfo']['actors']))

# a=int(input())
# if a > 5:
#     print('정답입니다.')# 조건문
# elif a==3:
#     print('반만 정답')
# elif a>2:
#     print('좋아요') # elif문은 바로 위의 조건이 거짓이고 나의 조건(elif)이 참이면 실행
# else:
#     print('오답입니다.') # else문 바로 위의 조건만 참이 아닐 경우 실행

# dust = 50
# dust = int(input())
# if dust > 150:
#     print("매우나쁨")
# elif 80 < dust <= 150:
#     print("나쁨")
# elif 30 < dust and dust <= 80:
#     print("보통")
# elif 0 <= dust <= 30:
#     print("좋음")

# 정수 1개를 입력받습니다. 입력받은 정수가 홀수인지 짝수인지 판별하여 출력하는 코드 완성하기
# a = int(input())
# if num % 2: # %는 modular operator or mod operator => 나머지 && 홀수,짝수판별 && 어떤 수의 배수판별
#     print(f"{num}은 홀수입니다.")
# elif num % 2 == 0:
#     print(f"{num}은 짝수입니다.")
# if a % 3 == 0:
#     print('a는 3의 배수')
# else:
#     print('a는 3의 배수가 아님')

# 반복문 for(가독성), while(무한루프)
# for i in range(1, 11):
#     print(i, end = ' ')
# i = 1
# while i <= 10: # 조건이 참인 동안에 실행
#     print(i, end = ' ')
#     i += 1
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # 리스트의 원소 중에서 홀수만 찾아서 그 값을 출력해 주세요~~~~~~
# for number in numbers:
#     if number % 2:
#         print(f"{number}은(는) 홀수입니다.")
# print()
# i = 0
# while i < len(numbers):
#     if numbers[i] % 2:
#         print(f"{numbers[i]}은(는) 홀수입니다.")
#     i += 1

# def abc(): # 함수를 정의한다!!  def 함수이름():
#     print(' ()   ()  ')
#     print('(        )')
#     print('(  0  0  )')
#     print('(    *   )')
#     print('(  \__/  )')
#     print(' ()   ()  ')
#     print()
# abc() # 함수를 호출한다.

# import random
# food = ['빵', '죽', '치킨', '피자', '오리탕', '창평국밥']
# #랜덤하게 1개를 뽑도록 하겠습니다.
# lunch = random.choice(food) # random.choice 랜덤하게 값을 1개 뽑을 때 사용
# print(lunch)
# dinner = random.sample(food,k = 2) # 랜덤하게 값을 여러개 뽑을 때 (중복 안함)
# print(dinner)
# breakfast = random.choices(food, k = 3) # 랜덤하게 값을 여러개 뽑을 때 (중복 허용)
# print(breakfast)

