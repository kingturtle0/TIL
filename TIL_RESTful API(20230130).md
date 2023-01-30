# RESTful API(REpresentational State Transfer)

REST는 Resource Oriented Architecture(리소스 지향 아키텍처)이다. API설계의 중심에 자원(Resource)이 있고 HTTP Method를 통해 자원을 처리하도록 설계하는 것이다.

- REST 6가지 원칙
  
  - Uniform Interface
  
  - Stateless
  
  - Caching
  
  - Client-Server
  
  - Hierarchical system
  
  - Code on demand

RESTful하게 API를 디자인 한다는 것은 무엇을 의미하는가.

1. 리소스와 행위를 명시적이고 직관적으로 분리한다.
   
   - 리소스는 **URI(Uniform Resuorce Identifier, 통합 자원 식별자)** 로 표현되는데 리소스가 가리키는 것은 **명사**로 표현되어야 한다.
   
   - 행위는 **HTTP Method**로 표현하고, GET(조회), POST(생성), PUT(기존 entity 전체 수정), PATCH(기존 entity 일부 수정), DELETE(삭제)을 분명한 목적으로 사용한다.

2. Message는 Header와 Body를 명확하게 분리해서 사용한다.
   
   - Entity에 대한 내용은 Body에 담는다.
   
   - 애플리케이션 서버가 행동할 판단의 근거가 되는 컨트롤 정보인 API 버전 정보, 응답받고자 하는 MIME타입 등은 Header에 담는다.


