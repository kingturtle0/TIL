JavaScript는 클라이언트 측 웹(브라우저)에서 실행하며, 웹 페이지가 이벤트 발생 시 어떻게 작동하는 지 디자인/프로그래밍 웹 페이지 동작을 제어하는데 널리 사용

### Web 기술의 기반이 되는 언어

- HTML 문서의 콘텐츠를 동적으로 변경할 수 있는 언어
- Web이라는 공간에서 채팅, 게임 등 다양한 동작을 할 수 있게 된 기반

## JavaScript Engine

- JavaScript Engine은 자바스크립트 코드를 실행하는 프로그램 또는 인터프리터
여러 목적으로 자바스크립트 엔진을 사용하지만, 대체적으로 웹 브라우저에서 사용

### 웹 브라우저의 역할

- URL을 통해 Web(WWW)을 탐색함
- HTML/CSS/JavaScript(구조/표현/동작)를 이해한 뒤 해석해서 사용자에게 하나의 화면으로 보여줌
- 웹 서비스 이용 시 클라이언트의 역할을 함
- 즉, 웹 페이지 코드를 이해하고, 보여주는 역할을 하는 것이 바로 웹 브라우저

### JavaScript Engine

- HTML/CSS/JavaScript를 이해한 뒤 해석 ⇒ JavaScript를 해석하는 것이 JavaScript Engine의 역할
- 각 브라우저마다 자체 JavaScript Engine을 개발, 사용
    - V8 - Chrome
    - Chakra - Microsoft Edge
    - JSC(JavaScript Core) - Apple (safari)
    - SpiderMonkey - FireFox
- 대체적으로 웹 브라우저에서 사용
- 웹 브라우저 외에는 Node.js(프레임워크, 라이브러리 X | 환경 O)에서 활용된다. Node.js는 V8엔진을 사용하여 서버 측에서 자바스크립트 코드를 실행 가능하다. 브라우저 조작 이외의 역할도 수행한다.

## JavaScript 실행 환경 구성

- Web Brower로 실행하기
    1. HTML 파일에 포함시키기 ⇒ 꼭 script는 닫는 body태그 바로 위에 넣기!
    2. 외부 JavaScript 파일 사용하기 ⇒ head에 포함
    3. Web Browser에서 바로 입력하기 ⇒ 브라우저에 엔진이 있으니까
- Chrome의 개발자 도구 - Console 탭에서 결과 확인 가능
- 특별하게 웹 브라우저에서 바로 실행할 수 있는 JavaScript 문법들을 Vanilla JavaScript라고 부름

### 정리

- 웹 브라우저는 JavaScript를 해석하는 엔진을 가지고 있음
- 특히, Chrome의 V8의 경우 JavaScript를 번역하는 속도가 매우 빠름 ⇒ 웹 브라우저 말고 다른 개발에서도 활용해보자
    - node.js, react.js, electron 등의 내부 엔진으로 사용됨. 그 결과 back-end, mobile, desktop app 등을 모두 JavaScript로 개발이 가능해짐

### EcmaScript

- Ecma International(전자 정보 통신 시스템 표준화 기구)이 ECMA-262 규격에 따라 정의하고 있는 표준화된 스크립트 프로그래밍 언어를 뜻함
- JavaScript를 표준화하기 위해 만들어짐
- JavaScript의 기본적인 문법, 데이터 타입, 객체 모델, 함수, 연산자 등을 정의
- 주석 : 한줄(`//`) 여러 줄(`/* */`)
- 들여쓰기와 코드블럭 : 2칸 들여쓰기, 블럭(block)은 if, for, 함수에서 중괄호 {}내부를 말함

## 변수와 식별자

- 식별자(identifier)는 변수를 구분할 수 있는 변수명을 말함
- 식별자는 반드시 문자, 달러($) 또는 밑줄(_)로 시작
- 대소문자를 구분, 클래스명 외에는 모두 소문자로 시작
- 예약어 사용 불가능 (예: for, if, function 등)

### 식별자 정의와 특징

- 카멜 케이스(camelCase) ⇒ 변수, 객체, 함수에 사용

```jsx
// 변수
let dog
let variableName
// 객체
const userInfo = {name: 'Tom', age: 20}
// 함수
function add() {}
function getName() {}
```

- 파스칼 케이스(PascalCase) ⇒ 클래스, 생성자에 사용

```jsx
// 클래스
class User {
	constructor(options) {
		this.name = options.name
	}
}
// 생성자 함수
function User(options) {
	this.name = options.name
}
```

- 대문자 스네이크 케이스(SNAKE_CASE) ⇒ 상수(constants)에 사용, 상수 : 개발자의 의도와 상관없이 변경될 가능성이 없는 값을 의미

```jsx
// 값이 바뀌지 않을 상수
const API_KEY = 'my-key'
const PI = Math.PI
//재할당이 일어나지 않는 변수
const NUMBERS = [1, 2, 3]
```

### 변수 선언 키워드

1. let : 블록 스코프 지역 변수를 선언 (추가로 동시에 값을 초기화)
2. const : 블록 스코프 읽기 전용 상수를 선언 (추가로 동시에 값을 초기화)
3. ~~var : 변수를 선언(추가로 동시에 값을 초기화)~~

### 선언, 할당, 초기화

- 선언(Declaration) : 변수를 생성하는 행위 또는 시점
- 할당(Assignment) : 선언된 변수에 값을 저장하는 행위 또는 시점
- 초기화(Initialization) : 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점

```jsx
let foo          // 선언
console.log(foo) // undefined
foo = 11         // 할당
console.log(foo) // 11
let bar = 0      // 선언 + 할당
console.log(bar) // 0
```

### 변수 선언 키워드 - let

- 재할당 가능 & 재선언 불가능
- 블록 스코프를 갖는 지역 변수를 선언, 선언과 동시에 원하는 값으로 초기화 할 수 있음

### 변수 선언 키워드 - const

- 재할당 불가능 & 재선언 불가능
- 선언 시 반드시 초기값을 설정해야 하며, 이후 값 변경이 불가능
- let과 동일하게 블록 스코프를 가짐

### 블록 스코프(block scope)

- if, for, 함수 등의 중괄호 ({}) 내부를 가리킴
- 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

### 변수 선언 키워드 - var

- 재할당 가능 & 재선언 가능
- ES6 이전에 변수를 선언할 때 사용되던 키워드
- 호이스팅되는 특성으로 인해 예기치 못한 문제 발생 가능, 따라서 ES6 이후부터는 var 대신 const와 let을 사용하는 것을 권장
- 함수 스코프를 가짐

### 함수 스코프(function scope)

- 함수의 중괄호 내부를 가리킴
- 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능

### 호이스팅(hoisting)

- 변수를 선언 이전에 참조할 수 있는 현상
- vara로 선언된 변수는 선언 이전에 참조할 수 있으며, 이러한 현상을 호이스팅이라 함
- 변수 선언 이전의 위치에서 접근 시 undefined를 반환
- 즉, JavaScriot에서 변수들은 실제 실행 시에 코드의 최상단으로 끌어 올려지게 되며(hoisted) 이러한 이유 때문에 var로 선언된 변수는 선언 시에 undefined로 값이 초기화되는 과정이 동시에 일어남
- 반면 **let, const**는 호이스팅이 일어나면 에러를 발생시킴
- 변수를 선언하기 전에 접근이 가능한 것은 코드의 논리적인 흐름을 깨뜨리는 행위이며 이러한 것을 방지하기 위해 let, const가 추가되었음. 즉, var는 사용하지 않아야 하는 키워드
- 다만, 아직까지도 많은 기존의 JavaScripte 코드는 ES6 이전의 문법으로 작성되어 있으므로 호이스팅에 대한 이해가 필요

| 키워드 | 재선언 | 재할당 | 스코프 | 비고 |
| --- | --- | --- | --- | --- |
| let | X | O | 블록 스코프 | ES6부터 도입 |
| const | X | X | 블록 스코프 | ES6부터 도입 |
| var | O | O | 함수 스코프 | 사용 X |

## 데이터 타입

- JavaScript의 모든 값은 특정한 데이터 타입을 가짐
- 크게 원시 타입(Primitive type)과 참조 타입(Reference type)으로 분류됨

### 원시 타입(Primitive type)

1. Number - 정수 또는 실수형 숫자를 표현하는 자료형
2. String - 문자열을 표현하는 자료형
3. null - 값이 없음을 나타냄
4. undefined - 값이 할당되지 않은 변수를 나타냄
5. Boolean - 참과 거짓을 표현하는 자료형
6. Symbol - 유일한 값을 표현하는 자료형 ES6에서 추가

### Number

- 정수, 실수, 지수형(1.2e8), 무한대(+-Infinity), Not a Number(NaN)
- NaN을 반환하는 경우
    1. 숫자로서 읽을 수 없음(`parseInt("어쩌구"), Number(undefined)` )
    2. 결과가 허수인 수학 계산식 (`Math.sqrt(-1)`)
    3. 피연산자가 NaN (`7**NaN`)
    4. 정의할 수 없는 계산식 (`0*Infinity`)
    5. 문자열을 포함하면서 덧셈이 아닌 계산식(`"가"/3`)

### String

- 문자열을 표현하는 자료형
- 작은 따옴표, 큰 따옴표 모두 가능
- 덧셈을 통해 문자열끼리 붙일 수 있음. 나머지 X
- 따옴표를 사용하면 선언 시 줄 바꿈 불가능. 대신 escape sequence 사용(\n)
- Template Literal을 사용하면 줄 바꿈이 가능, 문자열 사이에 변수도 삽입 가능

### Template literals

- 내장된 표현식을 허용하는 문자열 작성 방식
- ES6+ 부터 지원
- Backtick(``)을 이용하며, 여러 줄에 걸쳐 문자열을 정의할 수도 있고 JavaScript의 변수를 문자열 안에 바로 연결할 수 있는 이점이 생김
- 표현식을 넣을 수 있는데, 이는 $와 중괄호(${expression})로 표기

### Empty Value

- 값이 존재하지 않음을 표현하는 값으로 JavaScript에서는 null과 undefined가 존재
- 동일한 역할을 하는 이 두 개의 키워드가 존재하는 이유는 단순한 JavaScript의 설계 실수

### null

- null 값을 나타내는 특별한 키워드
- 변수의 값이 없음을 의도적으로 표현할 때 사용

### undefined

- 값이 정의되어 있지 않음을 표현하는 값
- 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 할당됨

### null과 undefined

- null과 undefined의 가장 대표적인 차이점은 typeof 연산자를 통해 타입을 확인했을 때 나타남

```jsx
typeof null // "object"
typeof undefined // "undefined"
```

- null이 원시 타입임에도 불구하고 object로 출력되는 이유는 JavaScript 설계 당시의 버그를 지금까지 해결하지 못한 것
- 쉽게 해결할 수 없는 이유는 이미 null타입에 의존성을 띄고 있는 많은 프로그램들이 망가질 수 있기 때문(하위 호환 유지)

### Boolean

- true와 false
- 조건문 또는 반복문에서 boolean이 아닌 데이터 타입은 자동 형변환 규칙에 따라 true 또는 false로 변환됨

### 참조 타입(Reference type)

1. Object - 이름과 값을 가진 속성(property)들의 집합으로 이루어진 자료구조
2. Array - 여러 개의 값을 순서대로 저장하는 자료구조
3. function - function 키워드를 통해 생성하며, 호출 시 실행될 코드를 정의

### 객체 (Object)

- 객체는 속성(property)의 집합이며, 중괄호 내부에 key와 value의 쌍으로 표현
- key
    - 문자열 타입만 가능
    - key이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현
- value
    - 모든 타입(함수포함) 가능
- 객체 요소 접근
    - 점(.) 또는 대괄호([])로 가능
    - key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능

### 배열(Array)

- 키와 속성들을 담고 있는 참조 타입의 객체
- 순서를 보장하는 특징이 있음
- 주로 대괄호([])를 이용하여 생성하고, 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능
- 배열의 길이는 array.length 형태로 접근 가능(마지막 원소는 array.length - 1로 접근)

### 함수(Function)

- 참조 타입 중 하나로써 function 타입에 속함
- JavaScript에서 함수를 정의하는 방법은 주로 2가지로 구분됨
- 함수 선언식 (function declaration)
- 함수 표현식 (function expression)

### 함수 선언식(Function declaration)

- 일반적인 프로그래밍 언어의 함수 정의 방식

```jsx
function 함수명 (매개변수) {
  // 어쩌구
}

function add (num1, num2) {
  return num1 + num2
}
add(2, 7) // 9
```

### 함수 표현식(Function expression)

- 표현식 내에서 함수를 정의하는 방식
- 함수 표현식은 함수의 이름을 생략한 익명 함수로 정의 가능

```jsx
변수키워드 함수명 = function (매개변수) {
  // 어쩌구
}

const sub = function (num1, num2) {
  return num1 - num2
}
sub(7, 2) // 5
```

- 표현식에서 함수 이름을 명시하는 것도 가능
- 다만 이 경우 함수 이름은 호출에 사용되지 못하고 디버깅 용도로 사용됨

```jsx
const mySub = function namedSub(num1, num2) {
	return num1 - num2
}
mySub(1, 2) // -1
namedSub(1, 2) // ReferenceError: namedSub is not defined
```

## 연산자

### 동등 연산자 (==)

- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
- 비교할 때 암묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
- **예상치 못한 결과가 발생할 수 있으므로 특별한 경우를 제외하고 사용하지 않음**

```jsx
const a = 1
const b = '1'

console.log(a == b) // true
console.log(a == true) // true

//자동 형변환 예시
console.log(8 * null) // 0, null은 0
console.log('5' - 1) // 4
console.log('5' + 1) // '51'
console.log('five' * 2) // NaN
```

### 일치 연산자 (===)

- 두 피연산자의 값과 타입이 모두 같은 경우 true를 반환
- 같은 객체를 가리키거나, 같은 타입이면서 같은 값인지를 비교
- 엄격한 비교(두 비교 대상의 타입과 값 모두 같은 지 비교하는 방식)가 이뤄지며 암묵적 타입 변환이 발생하지 않음

### 논리 연산자

- 세 가지 논리 연산자로 구성
    - and 연산은 `&&` 연산자
    - or 연산은 `||` 연산자
    - not 연산은 `!` 연산자
- 단축 평가 지원
- `false && true` ⇒ false
- `true || false` ⇒ true

### 삼항 연산자(Ternary Operator)

- 3개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자
- 가장 앞의 조건식이 참이면 :(콜론) 앞의 값이 반환되며, 그 반대일 겨우 뒤의 값이 반환되는 연산자
- 삼함 연산자의 결과 값이기 때문에 변수에 할당 가능

```jsx
true ? 1:2 // 1
false ? 1:2 // 2
const result = Math.PI > 4 ? 'Yep':'Nope'
console.log(result) // Nope
```

### 스프레드 연산자(Spread Operator)

- 배열이나 객체를 전개하여 각 요소를 개별적인 값으로 분리하는 연산자
- 주로 함수 호출 시 매개변수로 배열이나 객체를 전달할 때 사용
- 얕은 복사를 위해서도 활용 가능

## 조건문

- if, else if, else
- 조건은 소괄호(condition)안에 작성
- 실행할 코드는 중괄호 안에 작성
- 블록 스코프 생성

## 반복문

### 반복문 종류

- while
- for
- for…in
- for…of
- Array.forEach

### while ⇒ 조건

- 조건문이 참이기만 하면 문장을 계속해서 수행

```jsx
let i = 0
while (i < 6) {
	console.log(i)
	i += 1
} // 0, 1, 2, 3, 4, 5
```

### for ⇒ 횟수

```jsx
for (let i = 0;i < 6;i++) {
	console.log(i)
} // 0, 1, 2, 3, 4, 5
```

### for … in

- 객체(object)의 속성을 순회할 때 사용(인덱스 출력)
- 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장하지 않음

```jsx
for (variable in object) {
  statements
}

const fruits = {a:'apple', b:'banana'}
for (const key in fruits) {
  console.log(key) // a, b
  console.log(fruits[key]) // apple, banana
}
```

### for … of

- 반복 가능한 객체를 순회할 때 사용(값 출력)
- 반복 가능한(iterable) 객체의 종류: Array, Set, String 등

```jsx
const numbers = [0, 1, 2, 3]
for (const number of numbers) {
	console.log(number) // 0, 1, 2, 3
}
```

### for…in과 for…of 차이

- for…in은 속성 이름을 통해 반복 ⇒ 객체 순회 적합
- for…of은 속성 값을 통해 반복 ⇒ Iterable 순회 적합

```jsx
const arr = [3, 5, 7]
for(const i in arr) {
	console.log(i) // 0 1 2
}
for(const i of arr) {
	console.log(i) // 3 5 7
}
```

### for …in, for …of와 const

- for(let i = 0; i < arr.length; i++) {…}의 경우에는 최초 정의한 i를 재할당 하면서 사용하기 때문에 const를 사용하면 에러 발생
- for …in, for …of의 경우에는 재할당이 아니라, 매 반복 시 해당 변수를 새로 정의하여 사용하므로 에러가 발생하지 않음

### Array.forEach()

- 배열의 메서드들 중 하나

```jsx
Array.forEach(function(params) {
	// 배열이 가진 각 요소를 순회하면서 함수를 실행, 실행 코드 작성
})
const numbers = [1, 2, 3]
numbers.forEach(function (element) {
	console.log(element)
}) // 1 2 3
```
## 함수

- 참조 타입 중 하나로써 function 타입에 속함
- JavaScript에서 함수를 정의하는 방법은 주로 2가지로 구분됨
    - 함수 선언식(function declaration) ⇒ 호이스팅 발생!
    - 함수 표현식(function expression)

### 기본 인자(Default arguments)

- 인자 작성 시 = 문자 뒤 기본 인자 선언 가능

```jsx
const greeting = function (name = 'Anonymous') {
  return `Hi ${name}`
}
greeting() // Hi Anonymous
```

### 매개변수와 인자의 개수 불일치 허용

- 매개변수보다 인자의 개수가 많을 경우

```jsx
const noArgs = function() {
	return 0
}
noArgs(1, 2, 3) // 0

const twoArgs = function (arg1, arg2) {
  return [arg1, arg2]
}
twoArgs(1, 2, 3) // [1, 2]
```

- 매개변수보다 인자의 개수가 적을 경우

```jsx
const threeArgs = function (arg1, arg2, arg3) {
	return [arg1, arg2, arg3]
}
threeArgs() // [undefined, undefined, undefined]
threeArgs(1) // [1, undefined, undefined]
threeArgs(2, 3) // [2, 3, undefined]
```

### Spread syntax (…)

- 전개 구문을 사용하면 배열이나 문자열과 같이 반복 가능한 객체를 배열의 경우는 요소, 함수의 경우는 인자로 확장할 수 있음
1. 배열과의 사용
2. 함수와의 사용(Rest parameters)

## 선언식과 표현식

### 함수의 타입

- 선언식 함수와 표현식 함수 모두 타입은 function으로 동일

### 호이스팅

- 함수 선언식으로 정의한 함수는 var로 정의한 변수처럼 호이스팅이 발생. 즉, 함수 호출 이후에 선언해도 동작함
- 반면 함수 표현식으로 선언한 함수는 정의 전에 호출 시 에러 발생
- 함수 표현식으로 정의된 함수는 변수로 평가되어 변수의 scope 규칙을 따름

## Arrow Function

### 화살표 함수

- 함수를 비교적 간결하게 정의할 수 있는 문법
- function 키워드와 중괄호를 이용한 구문을 짧게 사용하기 위해 탄생
    1. function 키워드 생략가능
    2. 함수의 매개변수가 하나 뿐이라면 매개변수의 () 생략 가능
    3. 함수의 내용이 한 줄이라면 {}와 return도 생략 가능
- 화살표 함수는 항상 익명 함수 === 함수 표현식에서만 사용가능

```jsx
const arrow1 = function (name) {
  return 'hello'
}
const arrow2 = (name) => {return 'hello'} // function 키워드 삭제
const arrow3 = name => {return 'hello'} // 인자가 1개일 경우만 () 생략 가능
const arrow4 = name => 'hello' // 함수 바디가 return을 포함한 표현식 1개일 경우에 {}, return 생략 가능
// 명확성과 일관성을 위해 항상 인자 주의에는 괄호()를 포함하는 것을 권장
let noArgs = () => 'No args' // 인자가 없다면 () or _로 표시 가능
noArgs = _ => 'No args' // _보다는 괄호() 권장
let returnObject = () => { return { key: 'value'} } // object를 return한다면 return을 명시적으로 적어준다.
returnObject = () => ({ key: 'value'}) // return을 적지 않으려면 괄호를 붙여야 함
```

### 즉시 실행 함수(일회용 함수)

- 한 번만 실행하고 없어지는 함수
- 한 번의 실행 만 필요로 하는 초기화 코드 부분에 많이 사용된다. 변수를 전역으로 너무 많이 선언하는 것을 피하기 위해서이다.
- 바로 위의 코드에 세미 콜론이 꼭 있어야 한다.

```
(function (params){
  console.log(params)
})(args)
(function (num) {
  console.log(num**3)
})(2) // 8
```

## this

- 어떠한 object를 가리키는 키워드(java에서의 this와 python에서의 self는 인스턴스 자기자신을 가리킴)
- JavaScript의 함수는 호출될 때 this를 암묵적으로 전달 받음
- JavaScript에서의 this는 일반적인 프로그래밍 언어에서의 this와 조금 다르게 동작
- JavaScript는 해당 함수 호출 방식에 따라 this에 바인딩 되는 객체가 달라짐
- 즉, 함수를 선언할 때 this에 객체가 결정되는 것이 아니고, 함수를 호출할 때 함수가 어떻게 호출 되었는지에 따라 동적으로 결정됨

### this INDEX

1. 전역 문맥에서의 this
2. 함수 문맥에서의 this
    - 단순 호출
    - Method (객체의 메서드로서)
    - Nested
3. 생성자 함수 문맥에서의 this

### 전역 문맥에서의 this

- 브라우저의 전역 객체인 window를 가리킴
- 전역 객체는 모든 객체의 유일한 최상위 객체를 의미

### 함수 문맥에서의 this

- this의 값은 함수를 호출한 방법에 의해 결정됨
- 함수 내부에서 this의 값은 함수를 호출한 방법에 의해 좌우됨
1. 단순 호출
    - 전역 객체를 가리킴
    - 브라우저에서 전역은 window를 의미함
2. Method (Function in Object, 객체의 메서드로서)
    - 메서드로 선언하고 호출한다면, 객체의 메서드이므로 해당 객체가 바인딩
3. Nested (Function 키워드)
    - forEach의 콜백 함수에서의 this가 메서드의 객체를 가리키지 못하고 전역 객체 window를 가리킴
    - 단순 호출 방식으로 사용되었기 때문
    - 이를 해결하기 위해 등장한 함수 표현식이 바로 화살표 함수
4. Nested (화살표 함수)
    - 이전에 일반 function 키워드와 달리 메서드의 객체를 잘 가리킴
    - 화살표 함수에서 this는 자신을 감싼 정적 범위
    - 자동으로 한 단계 상위의 scope의 context를 바인딩

### 생성자 함수 문맥에서의 this

- 미래에 생성될 인스턴스를 의미

### 화살표 함수

- 화살표 함수는 호출의 위치와 상관없이 상위 스코프를 가리킴(Lexical scope this)
- Lexical scope
    - 함수를 어디서 호출하는지가 아니라 어디에 선언하였는지에 따라 결정
    - Static scope라고도 하며 대부분의 프로그래밍 언어에서 따르는 방식
- 따라서 함수 내의 함수 상황에서 화살표 함수를 쓰는 것을 권장

### Lexical scope

- 함수를 어디서 호출하는지가 아니라 어디에 선언하였는지에 따라 결정

```jsx
let x = 1 // global
function first() {
  let x = 10
	second()
}
function second() {
  console.log(x)
}
first() // 1
second() // 1
```

### this 정리

- 이렇게 this가 런타임에 결정되면 장점도 있고 단점도 있음
- 함수(메서드)를 하나만 만들어 여러 객체에서 재사용할 수 있다는 것은 장점이지만, 이런 유연함이 실수로 이어질 수 있다는 것은 단점
- JavaScript가 this를 다루는 방식이 좋은지, 나쁜지는 우리가 판단할 문제가 아니고 중요한 것은 개발자는 this의 동작 방식을 충분히 이해하고 장점을 취하면서 실수를 피하는 데만 집중.
- obj.functioncall() → this === obj, 다른 경우 this === window object(global)

## Array와 Object

- JavaScript의 데이터 타입 중 참조 타입(reference)에 해당하는 타입은 Array와 Object이며, 객체라고도 말함
- 객체는 속성들의 모음

## 배열(Array)

- 키와  속성들을 담고 있는 참조 타입의 객체
- 순서를 보장하는 특징이 있음
- 주로 대괄호[]를 이용하여 생성하고, 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능
- 배열의 길이는 array.length형태로 접근 가능

## 배열 메서드 기초

- array.reverse() : 원본 배열 요소들의 순서를 반대로 정렬
- array.push() : 배열의 가장 뒤에 요소 추가
- array.pop() : 배열의 마지막 요소 제거
- array.includes(value) : 배열에 특정 값(value)이 존재하는지 판별 후 true 또는 false 반환
- array.indexOf(value) : 배열에 특정 값이 존재하는지 확인 후 가장 첫 번째로 찾은 요소의 인덱스 반환. 없으면 -1 반환

## 배열 메서드 심화

### Array Helper Methods

- 배열을 순회하며 특정 로직을 수행하는 메서드
- 메서드 호출 시 인자로 callback함수를 받는 것이 특징
- callback 함수 : 어떤 함수의 내부에서 실행될 목적으로 인자를 넘겨받는 함수

### 콜백 함수

- 다른 함수의 인자로 전달되는 함수를 콜백 함수라고 한다.

### forEach

```jsx
array.forEach(function (element, index, array) {
  //do something
})
```

- array.forEach(callback(element[, index[,array]]))
- 인자로 주어지는 함수(콜백 함수)를 배열의 각 요소에 대해 한 번씩 실행
- element : 배열의 요소
- index : 배열 요소의 인덱스
- array : 배열 그 자체
- **반환 값 없음**

### map

- array.map(callback(element[, index[, array]]))
- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- **콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환**
- 기존 배열 전체를 다른형태로 바꿀 때 유용 ⇒ forEach + return이라고 생각하기

### filter

- array.filter(callback(element[, index[, array]]))
- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- **콜백 함수의 반환 값이 true인 요소들만 모아서 새로운 배열 반환**
- 기존 배열의 요소들을 필터링할 때 유용

### reduce

- array.reduce(callback(acc, element, [index[, array]])[, initalValue])
- 인자로 주어지는 함수(콜백 함수)를 배열의 각 요소에 대해 한 번씩 실행해서, 하나의 결과 값을 반환
- 즉, 배열을 하나의 값으로 계산하는 동작이 필요할 때 사용(총합, 평균 등)
- map, filter 등 여러 배열 메서드 동작을 대부분 대체할 수 있음
- reduce 메서드의 주요 매개변수
    - acc : 이전 callback 함수의 반환 값이 누적되는 변수
    - initialValue (optional) : 최초 callback 함수 호출 시 acc에 할당되는 값, default값은 배열의 첫 번째 값
- reduce의 첫 번째 매개변수인 콜백함수의 첫 번째 매개변수(acc)는 누적된 값(전 단계까지의 결과)
- reduce의 두 번째 매개변수인 initialValue는 누적될 값의 초기값, 지정하지 않을 시 첫 번째 요소의 값이 됨, 빈 배열의 경우 initialValue를 제공하지 않으면 에러 발생

### find

- array.find(callback(element[, index[, array]]))
- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- 콜백 함수의 반환 값이 true면, 조건을 만족하는 첫 번째 요소를 반환
- 찾는 값이 배열에 없으면 undefined 반환

### some

- array.some(callback(element[, index[, array]]))
- 배열의 요소 중 하나라도 주어진 판별 함수를 통과하면 true반환
- 모든 요소가 통과하지 못하면 거짓 반환
- 빈 배열은 항상 false 반환

### every

- array.every(callback(element[, index[, array]]))
- 배열의 모든 요소가 주어진 판별 함수를 통과하면 true반환
- 하나의 요소라도 통과하지 못하면 거짓 반환
- 빈 배열은 항상 true 반환

## 객체 (Object)

- 객체는 속성(property)의 집합이며, 중괄호 내부에 key와 value의 쌍으로 표현
- **key**
    - 문자열 타입만 가능
    - key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현
- **value**
    - 모든 타입(함수포함) 가능
- 객체  요소 접근
    - 점(.) 또는 대괄호([])로 가능
    - key이름에 띄어쓰기 같은구분자가 있으면 대괄호 접근만 가능
- 객체는 속성으로 함수를 정의할 수 있음(메서드)

### 생성자 함수

- JS에서 객체를 하나 생성한다고 하면 ⇒ 하나의 객체를 선언하여 생성
- 동일한 형태의 객체를 또 만든다면 ⇒ 또 다른 객체를 선언하여 생성
- 불편하다 ⇒ new 연산자로 사용하는 함수
- 함수 이름은 반드시 대문자로 시작, 반드시 new연산자를 사용

```jsx
function Member(name, age, sId) {
	this.name = name
	this.age = age
	this.sId = sId
}
const member3 = new Member('isaac', 21, 2022654321)
```

## 객체 관련 문법

### 1. 속성명 축약

- 객체를 정의할 때 key와 할당하는 변수의 이름이 같으면 예시와 같이 축약 가능

```jsx
const books = ['Learning JavaScript', 'Learning Python']
const magazines = ['Vogue', 'Science']
const bookShop = {
	books: books,                  // =>
	magazines: magazines,
}
console.log(bookShop)
```

```jsx
const books = ['Learning JavaScript', 'Learning Python']
const magazines = ['Vogue', 'Science']
const bookShop = {
	books,
	magazines,
}
console.log(bookShop)
```

### 2. 메서드명 축약

- 메서드 선언 시 function 키워드 생략 가능

```jsx
var obj = {
  greeting: function () {
    console.log('Hi!')
  }
}
obj.greeting() // Hi!
```

```jsx
var obj = {
  greeting() {
    console.log('Hi!')
  }
}
obj.greeting() // Hi!
```

### 3. 계산된 속성(computed property name)

- 객체를 정의할 때 key의 이름을 표현식을 이용하여 동적으로 생성 가능

```jsx
const friends = ['kevin', 'kate', 'jorny'];
const age = [27, 29, 25];

let index=1;
const school = {
  friends,
  age,
  [friends[index]]:age[index],
};
console.log(school);
```

### 4. 구조 분해 할당(destructuring assignment)

- 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법

```jsx
const user = {
  name1:'minho',
  name2:'bbq',
  gender:'male',
}
console.log(user.name1, user.gender)

const {name1} = user;  // === const name1 = user.name
const {gender} = user; // === const gender = user.gender
console.log(name1, gender);
```

### 5. Spread syntax(…)

- 배열과 마찬가지로 전개구문을 사용해 객체 내부에서 객체 전개 가능
- 얕은 복사에 활용 가능

### JSON

- JavaScript Object Notation
- Key-Value 형태로 이루어진 자료 표기법
- JavaSCript의 Object와 유사한 구조를 가지고 있지만 Object는 그 자체로 타입이고, JSON은 형식이 있는 문자열
- **즉, JSON을 Object로 사용하기 위해서는 변환 작업이 필요**
- JSON 형식에는 JS와 다르게 key에는 반드시 쌍따옴표가 들어간다. 그래서 JS객체를 JSON형태로 변환할 때 key값에 쌍따옴표를 넣어줘야 한다. 이 때, JSON.stringify를 사용해서 객체를 string화 시킨 후 JSON형태로 변환이 된다.

```jsx
const jsObject = {
  coffee: 'Americano',
  iceCream: 'Gugu crust',
  test:[1,2,3,4],
};
console.log(jsObject)

const objToJson = JSON.stringify(jsObject);
console.log(objToJson)
console.log(typeof objToJson)

// Django와 같은 API서버에서 JSON을 응답한 것을 받아 다음과 같이 변환해야 한다.
const jsonToObj = JSON.parse(objToJson)
console.log(jsonToObj)
console.log(typeof jsonToObj)
```

### 배열은 객체다

- 배열은 키와 속성들을 담고 있는 참조 타입의 객체
- 배열은 인덱스를 키로 가지며 length 프로퍼티를 갖는 특수한 객체

## DOM

- 브라우저에서의 JavaScript
- JavaScript는 웹 페이지에서 다양한 기능을 구현하는 스크립트 언어
- 정적인 정보만 보여주던 웹 페이지를 데이터가 주기적으로 갱신되거나, 사용자와 상호작용을 하거나 애니메이션 등이 동작하게 하는 것을 가능하게 함
- 스크립트 언어(Script Language)란 기존에 존재하는 응용 소프트웨어를 제어하는 컴퓨터 프로그래밍 언어

### 웹 페이지에서의 JavaScript

- JS는 프로그래밍 언어로서의 역할도 가능하지만 클라이언트 사이드 JS언어 위에 올라가 있는 기능들은 더 다양함
- API라고 부르는 이 기능들은 JS 코드에서 사용할 수 있는 것들을 더 무궁무진하게 만들어 줌
- 이 API는 일반적으로 2개의 범주로 분류
    1. Browser APIs
    2. Third party APIs
        - 브라우저에 탑재되지 않은 API
        - 웹에서 직접 코드와 정보를 찾아야 함
        - Google map api, kakao login api 등

### Browser APIs

- 웹 브라우저에 내장된 API로, 웹 브라우저가 현재 컴퓨터 환경에 관한 데이터를 제공하거나, 오디오를 재생하는 등 여러가지 유용하고 복잡한 일을 수행할 수 있게 함
- JavaScript로 Browser API들을 사용해서 여러가지 기능을 사용할 수 있음
- 종류
    - **DOM**
    - Geolocation API
    - WebGL 등

### 브라우저가 웹 페이지를 불러오는 과정

- 웹 페이지를 브라우저로 불러오면, 브라우저는 코드(HTML, CSS, JS)를 실행 환경(브라우저 탭)에서 실행
- JS는 DOM API를 통해 HTML과 CSS를 동적으로 수정, 사용자 인터페이스를 업데이트하는 일에 가장 많이 쓰임

### DOM(Document Object Model)

- 문서 객체 모델
- 문서의 구조화된 표현을 제공하며 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공
    - 문서 구조, 스타일, 내용 등을 쉽게 변경할 수 있게 도움
    - HTML 콘텐츠를 추가, 제거, 변경하고, 동적으로 페이지에 스타일을 추가하는 등 HTML/CSS를 조작할 수 있음
- HTML 문서를 구조화하여 각 요소를 객체(object)로 취급
- 단순한 속성 접근, 메서드 활용 뿐만 아니라 프로그래밍  언어적 특성을 활용한 조작이 가능함
- DOM은 문서를 논리 트리로 표현
- DOM 메서드를 사용하면 프로그래밍적으로 트리에 접근할 수 있고 이를 통해 문서의 구조, 스타일, 컨텐츠를 변경할 수 있음
- 웹 페이지는 일종의 문서(document)
- 이 문서는 웹 브라우저를 통해 그 내용이 해석되어 웹 브라우저 화면에 나타나거나 HTML 코드 자체로 나타나기도 함
- DOM은 동일한 문서를 표현하고, 저장하고, 조작하는 방법을 제공
- DOM은 웹 페이지의 객체 지향 표현이며, JS와 같은 스크립트 언어를 이용해 DOM을 수정할 수 있음

## DOM 기본 구조

### DOM Tree

- DOM은 문서를 논리 트리로 표현
- DOM에서 모든 것은 Node
- 즉, HTML 요소, 속성, 텍스트 모든 것이 노드
- 각 노드느 부모, 자식 관계를 형성하고 이에 따라 상속 개념도 동일하게 적용됨

### Node

- DOM의 구성 요소 중 하나
- HTML 문서의 모든 요소를 나타냄
    - 각각의 HTML 요소는 DOM Node로서 특정한 노드 타입을 가짐
    - Document Node === HTML 문서 전체를 나타내는 노드
    - Element Node === HTML 요소를 나타내는 노드 ex) <p>
    - Text Node === HTML 텍스트, Element Node 내의 텍스트 컨텐츠를 나타냄
    - Attribute Node === HTML 요소의 속성을 나타내는 노드

### DOM에 접근하기

- DOM을 사용하기 위해 특별히 해야 할 일은 없음
- 모든 웹 브라우저는 스크립트 언어가 손쉽게 웹 페이지의 요소에 접근할 수 있도록 만들기 위해 DOM 구조를 항상 사용
- DOM의 주요 객체들을 활용하여 문서를 조작하거나 특정 요소들을 얻을 수 있음

### DOM의 주요 객체

- **window**
- **document**
- navigator, location, history, screen 등

### window object

- DOM을 표현하는 창
- 가장 최상위 객체 (작성 시 생략 가능)
- 탭 기능이 있는 브라우저에서는 각각의 탭을 각각의 window객체로 나타냄

```jsx
window.open() // 새 탭 열기
window.alert() // 경고 대화 상자 표시
window.print() // 인쇄 대화 상자 표시
```

### document object

- 브라우저가 불러온 웹 페이지
- 페이지 컨텐츠의 진입점 역할을 하며, <body>등과 같은 수많은 다른 요소들을 포함하고 있음
- document는 window의 속성

### DOM 조작

1. 선택(Select)
2. 조작(Manipulataion) : 생성, 추가, 삭제 등

### 선택 관련 메서드

- **document.querySelector(selector)**
    - 제공한 선택자와 일치하는 element 한 개 선택
    - 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환 (없다면 null 반환)
- **document.querySelectorAll(selector)**
    - 제공한 선택자와 일치하는 여러 element를 선택
    - 매칭할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
    - 제공한 CSS selector를 만족하는 NoedList(유사 배열)를 반환

### NodeList

- DOM 메서드를 사용해 선택한 노드의 목록
- 배열과 유사한 구조를 가짐
- Index로만 각 항목에 접근 가능
- 배열의 forEach메서드 및 다양한 배열 메서드 사용 가능(push()나 pop() 안됨)
- querySelectorAll()에 의해 반환되는 NodeList는 DOM의 변경사항을 실시간으로 반영하지 않음

### 조작 관련 메서드 (생성)

- **document.createElement(tagName)**
    - 작성한 tagName의 HTML요소를 생성하여 반환

### 조작 관련 메서드 (입력)

- Element**.innerText**
    - Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현(해당 요소 내부의 raw text)
    - 사람이 읽을 수 있는 요소만 남김(style이 hidden이면 값도 빈 값)
    - 즉, 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현됨

### 조작 관련 메서드 (추가)

- **Node.appendChild()**
    - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입
    - 한 번에 오직 하나의 Node만 추가할 수 있음
    - 추가된 Node 객체를 반환
    - 새롭게 생성한 Node가 아닌 이미 문서에 존재하는 Node를 다른 Node의 자식으로 삽입하는 경우, 위치를 이동

### 조작 관련 메서드 (삭제)

- **Node.removeChild()**
    - DOM에서 자식 Node를 제거
    - 제거된 Node를 반환

### 속성 조회 및 설정

- **Element.getAttribute(attributeName)**
    - 해당 요소의 지정된 값(문자열)을 반환
    - 인자(attributeName)는 값을 얻고자 하는 속성의 이름
- **Element.setAttribute(name, value)**
    - 지정된 요소의 값을 설정
    - 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가
- 그 외 다양한 속성 조작 방법
- 기존 속성은 유지한 채로, 새로운 값을 추가하고자 한다면 Element.classList, Element.style 등을 통해 직접적으로 해당 요소의 각 속성들을 제어할 수 있음

### DOM 조작 정리

1. 선택
    - querySelector()
    - querySelectorAll()
2. 조작
    - innerText
    - setAttribute()
    - getAttribute()
    - createElement()
    - appendChild()
    - …

## Event

- Event란 HTML 요소에서 발생하는 모든 상황을 의미
    - 예를 들어 사용자가 웹 페이지의 버튼을 클릭한다면 클릭에 대해 이벤트가 발생하고 우리는 이벤트를 통해 클릭이라는 사건에 대한 결과를 받거나, 조작을 할 수 있음
- 클릭 말고도 웹에서는 다양한 Event가 존재
    - 키보드 키 입력, 브라우저 닫기, 데이터 제출, 텍스트 복사 등

### Event object

- 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
- 이벤트가 발생했을 때 생성되는 객체
- Event 발생은 마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수도 있고 특정 메서드를 호출하여 프로그래밍적으로도 만들어 낼 수 있음
- DOM 요소는 Event를 받고(수신)
- 받은 Event를 처리할 수 있음
- Event처리는 주로 **addEventListener()**메서드를 통해 Event처리기(Event handler)를 다양한 html요소에 부착해서 처리함

### Event handler

- 특별한 함수가 아닌 일반적인 JavaScript Function을 정의하여 사용
- 웹 페이지에서 발생하는 Event에 대해 반응하여 동작하는 함수를 지칭
- Event handler 함수는 이벤트가 발생했을 때 호출되며, Event 객체를 매개 변수로 전달받음

### Event handler - `addEventListener()`

<aside>
💡 대상에 특정 Event가 발생하면, 할 일을 등록하자

EventTarget.addEventListener(type, handler function)

</aside>

- EventTarget.addEventListener(type, handler function[, options])
- 지정한 Event가 대상에 전달될 때마다 호출할 함수를 설정
- Event를 지원하는 모든 객체(Element, Document, Window 등)를 대상(EventTarget)으로 지정 가능
- type : 반응할 Event 유형을 나타내는 대소문자 구분 문자열(input, click, submit, …)
- handler function : 지정된 타입의 Event를 수신할 객체, JS function객체(콜백 함수)여야 함, 콜백 함수는 발생한 Event의 데이터를 가진 Event 객체를 유일한 매개변수로 받음

## Event 전파와 취소

### Event 전파란?

- DOM 요소에서 발생한 이벤트가 상위 노드에서 하위 노드 혹은, 하위 노드에서 상위 노드로 전파되는 현상을 의미
- addEventListener 메서드를 사용하여 전파 방식을 제어할 수 있음
기본 값은 하위 노드에서 상위 노드로 전파되는 방식을 사용 - Event Bubbling
- 또한, 이러한 이벤트 전파 상황을 필요에 따라 제어할 수도 있음

### event.preventDefault()

- 현재 Event의 기본 동작을 중단
- HTML 요소의 기본 동작을 자동하지 않게 막음
- HTML 요소의 기본 동작 예시
    - a 태그 : 클릭 시 특정 주소로 이동
    - form 태그 : form 데이터 전송

### lodash

- 모듈성, 성능 및 추가 기능을 제공하는 JavaScript 유틸리티 라이브러리
- array, object 등 자료구조를 다룰 때 사용하는 유용하고 간편한 유틸리티 함수들을 제공

### this와 addEventListener

- addEventListener에서의 콜백 함수는 특별하게 function 키워드의 경우 addEventListener를 호출한 대상을 (event.target) 뜻함
- 반면 화살표 함수의 경우 상위 스코프를 지칭하기 때문에 window객체가 바인딩 됨
- 즉, addEventListener의 콜백 함수는 function 키워드를 사용하자
