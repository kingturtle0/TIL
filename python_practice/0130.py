# 클래스, 객체, 인스턴스, 메서드가 무엇인지?
# 클래스 변수, 인스턴스 변수
# 클래스 메서드, 인스턴스 메서드, 정적 메서드(static method)

# 객체지향 프로그래밍이 무엇을 말하는지?
# ex) 게임 캐릭터 => name, hp, mp, skill*3 
# name=olaf, hp=100, mp=50, q=q(), w=w(),e=e()
# 클래스는 속성(변수)과 메서드로 나뉜다.

# class Calculator():
#     numberOfCal = 0 # 속성(클래스 변수)

#     def __init__(self): # __init__은 생성자(constructor)이다. 객체를 만들 때 첫 번째로 자동실행
#         self.result = 0 # 얘도 속성인데 얘는 인스턴스 변수이다.
#         Calculator.numberOfCal += 1

#     def getsum(self, value): # 클래스 안의 함수를 메서드라고 할 수 있겠다. 
#         self.result += value
#         return self.result

# cal1 = Calculator() # cal1이라는 객체(Calulator클래스의 인스턴스) 만들기
# print(cal1.getsum(3))
# print(cal1.getsum(4))
# print(cal1.getsum(5))

# 인스턴스 변수란? 인스턴스가 개인적으로 가지고 있는 속성(attribute)
# cal2 = Calculator()
# print(cal2.getsum(6))
# print(cal2.getsum(7))
# print(cal2.getsum(1))

# 클래스 변수란? 한 클래스의 모든 인스턴스가 공유하는 값을 의미
# print(cal1.numberOfCal)
# print(cal1.numberOfCal)
# print(Calculator.numberOfCal)

# 클래스 변수 값 변경 시 항상 클래스.클래스변수 형식으로 변경해야 한다.
# Calculator.numberOfCal = 6이 맞는 형식
# 객체.클래스변수는 틀린 형식, 밑은 틀린 형식의 예
# cal1.numberOfCal = 10
# print(cal1.numberOfCal) # 10 새로운 인스턴스 변수가 만들어진 것이다.
# print(cal2.numberOfCal) # 2

# Calculator.numberOfCal = 20 # 클래스 변수의 값을 바꿔도 
# print(cal1.numberOfCal) # 10 cal1은 바뀌지 않는 문제가 발생한다.
# print(cal2.numberOfCal) # 20

# 클래스 변수 : 모든 인스턴스가 공유한다. 인스턴스 전체가 사용해야 하는 값을 저장할 때 사용한다.
# 인스턴스 변수 : 인스턴스별로 독립되어 있다. 각 인스턴스가 값을 따로 저장해야 할 때 사용한다.


# 생성자 함수 없이 객체에 숫자 두 개를 넣으면 두 수의 더한 값과 뺀 값을 돌려주는 클래스 만들기
# class PlusMinus:
#     # 생성자 함수 없이 만들기
#     # def data(self, first, second): # 인자값으로 객체 a, 3, 5를 각각 뜻한다.
#     #     self.first = first
#     #     self.second = second

#     # 생성자 함수 사용하기
#     def __init__(self, first, second): # 매직 메서드
#         self.first = first
#         self.second = second

#     def plus(self):
#         return self.first + self.second

#     def minus(self):
#         return self.first - self.second

# a = PlusMinus()
# a.data(3, 5)
# b = PlusMinus()
# b.data(2, 7)
# print(a.first, b.first) # 3 2
# print(a.plus(), a.minus()) # 8 -2
# print(b.plus(), b.minus()) # 9 -5

# 객체 a와 b는 각각 독립적이다.
# 여기서 data가 바로 인스턴스 메서드이고 인스턴스 메서드는 self를 항상 첫 번째 parameter로 사용한다.
# 인스턴스 메서드는 클래스 자체에서 메서드 호출이 불가하고 인스턴스 변수를 통해서 메서드를 호출한다.

# c = PlusMinus(3, 5) # 인스턴스 만들 때 입력해주면 자동!
# print(c.plus(), c.minus())

# __init__ 매직메서드 (init add str 등) => 인스턴스 생성하자마자 자동호출 !!
# 파이썬에서 문자열에서 + 연산자를 사용하면 두 문자열이 합쳐지는 것은 클래스 안에 정의해 놓았기 때문이다.

# class Car:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __add__(self, another):
#         return self.price + another.price

#     def __str__(self):
#         return f'{kia.name}의 가격은 {kia.price}입니다.'

# kia = Car('k8', 300)
# bmw = Car('m5', 500) 
# print(kia.price + bmw.price) # 귀찮으니 아래처럼 커스터마이징 하자
# print(kia + bmw) # __add__ 매직메서드로 커스터마이징해서 덧셈 연산을 지원하도록 하겠다.

# print(f'{kia.name}의 가격은 {kia.price}입니다.') # 귀찮으니 아래처럼 커스터마이징 하자
# print(kia) # __str__ 매직메서드로 커스터마이징해서 바로 문자열 출력하도록 하겠다.
# del kia # 인스턴스 삭제
# print(kia) # error

# 데코레이터 : 함수를 하나 만드는데 그 함수를 직접 수정하지 않고 함수에 기능 추가하고자 할 때 사용
# 1. 데코레이터 사용 안 한 예
# def call_name(name):
#     print('반짝'*5)
#     print(name)
#     print('샤방'*5)

# def call_age(age):
#     print('반짝'*5)
#     print(age)
#     print('샤방'*5)

# def call_nickname(nick):
#     print('반짝'*5)
#     print(nick)
#     print('샤방'*5)

# call_name('거북')
# call_age(100)

# 2. 데코레이터 사용한 예
# def deco(func):

#     def wrapping(value):
#         print('반짝'*5)
#         func(value)
#         print('샤방'*5)
    
#     return wrapping

# @deco
# def call_name(name):
#     print(name)

# @deco
# def call_age(age):
#     print(age)

# call_name('거북')
# call_age(100)

# 정적 메서드
# class car:
#     @staticmethod # 정적메서드에는 @staticmethod를 붙인다. self가 없다.(self는 인스턴스 메서드에 사용)
#     def add_price(one, another):
#         print(one + another)

# car.add_price(400, 800)
# 정적 메서드를 호출할 때는 클래스에서 바로 메서드를 호출하면 된다. 클래스의 인스턴스가 없어도 문제될 것 없다.
# self와 같은 속성을 다루지 않고 단지 함수의 행동(기능, 메서드내용)만 하는 메서드를 클래스에 정의할 때 사용한다.
# 그래서 호출할 때 클래스에서 바로 메서드를 호출한다.
# 그러나 인스턴스가 있다면 인스턴스로도 static method에 접근이 파이썬에서 가능하다.
# a7 = car()
# a7.add_price(500, 600)
# 이렇게 인스턴스로 정적 메서드 호출은 잘 하지 않는다.
# 그 이유는 이 정적메서드는 클래스의 인스턴스에 어떠한 변화도 일으키지 않는 함수라는 의미를 내포하고 암시할 때 사용하기 때문이다.

# 클래스 메서드
class MakePie:
    cnt = 0

    def __init__(self, name):
        self.name = name
        MakePie.cnt += 1
    
    @classmethod # @classmethod라는 데코레이터를 사용한다.
    def number_of_pies(cls): # 호출 시 첫 번째 인자로 항상 cls를 사용하고 cls는 속해있는 클래스 자체를 의미한다.
        print(f'파이를 {cls.cnt}명이 만들고 있습니다.')

    @classmethod
    def create(cls, name): # 클래스 내부에서 클래스 안의 메서드를 호출하는 함수
        c_name = cls(name)
        return c_name

a = MakePie('turtle1')
b = MakePie('turtle2')
c = MakePie('turtle3')

MakePie.number_of_pies() # 3
# 인스턴스에 a.number_of_pies()와 같이 사용은 가능하나 클래스 메서드를 사용한다는 의미를 내포하므로 클래스.메서드()로 이해하자

MakePie.create('turtle4') # 인스턴스를 만든 건 아니지만 생성자 함수를 호출하면서 개수를 하나씩 늘려준다.
MakePie.create('turtle5') # 클래스 메서드는 인스턴스 변수 없이 클래스 자체에서 클래스 속성이나 메서드에 접근이 가능하다.

MakePie.number_of_pies() # 5