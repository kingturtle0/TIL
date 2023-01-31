class PlusMinus:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def plus(self):
        result = self.first + self.second
        return result

    def minus(self):
        result = self.first - self.second
        return result

class MoreFunction(PlusMinus):
    def __init__(self, first, second, third):
        super().__init__(first, second) # super는 부모클래스의 init메서드를 그대로 호출하는 것
        self.third = third # third만 추가

    def mul(self):
        result = self.first * self.second * self.third
        return result

# b = MoreFunction(3,4,5)
# print(b.mul())
# print(b.plus())
# 자식클래스에서 생성된 메서드를 부모클래스에서 사용은 불가능!

# 오버라이딩이란 덮어쓰기를 말한다.
# 부모클래스에 있는 메서드를 동일한 이름으로 자식클래스에서 다시 만드는 것이다.
# 메서드 이름과 기본 기능은 그대로 사용하지만, 특정 기능을 바꾸고 싶을 때 사용한다.

class MoreFunction(PlusMinus):
    def __init__(self, first, second, third):
        super().__init__(first, second) # super는 부모클래스의 init메서드를 그대로 호출하는 것
        self.third = third # third만 추가

    def plus(self):
        get_sum = self.first + self.second + self.third
        if get_sum > 100:
            return '버그'
        else:
            return get_sum

    # 이렇게 부모클래스의 plus 메서드를 재정의하는 것을 메서드 오버라이딩이라고 한다.
    # 메서드 오버라이딩을 했지만, 부모클래스의 원래의 plus메서드를 또 사용하고 싶다면
    # 이 때, super()를 이용할 수 있다.
    def parents_plus(self):
        ret = super().plus() # 부모 메서드에서의 plus메서드 호출시 super활용
        return ret

# c = MoreFunction(1,1,99)
# print(c.plus())
# d = MoreFunction(500, 400, 200)
# print(d.parents_plus())
# print(MoreFunction.mro()) # method resolution order(상속 구조) 확인

# 캡슐화를 통해 외부 접근을 제어하는데 3가지가 있다.
# 접근       제어자    문법의미
# Public     name     외부로부터 모든 접근 허용
# Protected  _name    자기 클래스 내부 혹은 상속받은 자식 클래스에서만 접근 허용
# Private    __name   자기 클래스 내부의 메서드에서만 접근 허용

# Public 평소에 쓰던 거
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# p1 = Person('김싸피', 30)
# print(p1.age)
# Person 클래스의 인스턴스인 p1은 이름(name)과 나이(age) 모두 접근 가능합니다.

# Protected : 암묵적 규칙에 의해 메서드를 호출 시 부모클래스 내부나 자식클래스에서만 호출이 가능하다.
# 그러나 강제성은 없으므로 실제로는 Public과 거의 동일하게 외부 접근가능하다. (효과는 없고 암묵적 규칙)
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
    def getage(self):
        return self._age
# p1 = Person('김싸피', 30)
# print(p1.getage())
# print(p1._age)

# Private
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def getage(self):
        return self.__age
# p2 = Person('아무개', 30)
# print(p2.name)
# print(p2.__age)
# 이렇게 언더스코어 2개를 통해 클래스 멤버 속성을 외부에 있는 인스턴스로 직접 접근을 제한했다.
# 그래서 print(p2.__age)라고 하면 속성이 직접적으로 출력이 안된다.

# getter 메서드와 setter메서드를 만들어서 사용하면 private속성 변경이나 접근이 가능하다.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def getter(self): # private한 속성값을 확인하고자 함 (getter 함수)
        return self.__age

    def setter(self, value): # private한 속성값을 변경하고자 함(setter 함수)
        self.__age = value

k = Person('turtle', 100)
print(k.getter())
k.setter(5)
print(k.getter())
# 클래스의 private한 속성값을 getter와 setter를 이용해서 확인 그리고 값 변경이 가능하다.

# 그 다음에는 위 코드를 좀 더 간단하게 적기 위한 데코레이터를 사용할 것이다.
# getter 메서드와 setter메서드는 각각 @property 그리고 @변수.setter라는 데코레이터를 사용한다.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    @property # getter 메서드
    def age(self): # 함수명도 비공개 변수명과 같도록
        return self.__age

    @age.setter # setter 메서드
    def age(self, value):
        self.__age = value

x = Person('turtle2', 500)
print(x.age) # @property 데코레이터 사용을 하면 메서드 호출시 ()를 생략한다.
x.age = 3 # 관례상 setter getter 함수명은 변수명을 따른다.
print(x.age)

# from collections import Counter

# lst = ['apple', 'mango', 'banana', 'mango', 'apple','mango','banana','mango','apple']
# print(Counter(lst))

# ret = dict(Counter(lst))
# print(ret)

# st = 'an apple mango'
# ret = dict(Counter(st))
# print(ret)

# ret = sorted(ret.items(), key = lambda x:x[1], reverse = True)
# print(ret[0])

# st = 'an apple mango'
# # st요소를 세어, 최빈값 n개를 반환한다.
# ret = Counter(st).most_common(1) # 가장 많은거 1개만
# print(ret)

# # 추가적으로 Counter를 가지고 덧셈 뺄셈도 지원합니다.
# a = Counter('apple')
# b = Counter('mango')
# print(a+b)
# print(a-b)

# # 두 문자열을 대조할 때 사용도 가능
# a.subtract(b)
# print(a)