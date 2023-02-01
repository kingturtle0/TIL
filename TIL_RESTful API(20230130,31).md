# RESTful API(REpresentational State Transfer)

REST는 Resource Oriented Architecture(리소스 지향 아키텍처)이다. API설계의 중심에 자원(Resource)이 있고 HTTP Method를 통해 자원을 처리하도록 설계하는 것이다.

### REST 6가지 원칙

- Uniform Interface

- Stateless

- Caching

- Client-Server

- Hierarchical system

- Code on demand

### RESTful하게 API를 디자인 한다는 것은 무엇을 의미하는가.

1. 리소스와 행위를 명시적이고 직관적으로 분리한다.
   
   - 리소스는 **URI(Uniform Resuorce Identifier, 통합 자원 식별자)** 로 표현되는데 리소스가 가리키는 것은 **명사**로 표현되어야 한다.
   
   - 행위는 **HTTP Method**로 표현하고, **GET(조회)**, **POST(생성)**, **PUT(기존 entity 전체 수정)**, **PATCH(기존 entity 일부 수정)**, **DELETE(삭제)**을 분명한 목적으로 사용한다.

2. Message는 Header와 Body를 명확하게 분리해서 사용한다.
   
   - Entity에 대한 내용은 body에 담는다.
   
   - 애플리케이션 서버가 행동할 판단의 근거가 되는 컨트롤 정보인 API 버전 정보, 응답받고자 하는 MIME타입 등은 header에 담는다.
   
   - header와 body는 http header와 http body로 나눌 수도 있고, http body에 들어가는 json구조로 분리할 수도 있다.

3. API버전을 관리한다.
   
   - 환경은 항상 변하기 때문에 API의 signature가 변경될 수도 있음에 유의하자.
   
   - 특정 API를 변경할 때는 반드시 하위호환성을 보장해야 한다.

4. 서버와 클라이언트가 같은 방식을 사용해서 요청하도록 한다.
   
   - 브라우저는 form-data형식의 submit으로 보내고 서버에서는 json형태로 보내는 식의 분리보다는 json으로 보내든, 둘 다 form-data형식으로 보내는 하나로 통일한다.
     즉, URI가 플랫폼 중립적이어야 한다.

### 장점

1. Open API를 제공하기 쉽다

2. 멀티플랫폼 지원 및 연동이 용이하다

3. 원하는 타입으로 데이터를 주고 받을 수 있다.

4. 기존 웹 인프라(HTTP)를 그대로 사용할 수 있다.

### 단점

1. 사용할 수 있는 메소드가 한정적이다.

2. 분산환경에는 부적합하다.

3. HTTP통신 모델에 대해서만 지원한다.

4. 


