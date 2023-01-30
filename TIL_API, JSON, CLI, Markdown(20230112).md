# TIL(Today I Learned) 2023/01/12

---

### API(Application Programming Interface)

---

- 사람들끼리 서버에 요청하는 규칙을 만들었는데 그 규칙을 **API**라고 한다.

- 우리는 서버가 만든 **API** 규칙에 맞춰 요청을 한다. 즉, 서버 개발자가 요청규칙(**API**)를 정한다.

- 이 때, 서버끼리 서버마다 요청하는 방식이 다르면 안되므로 통일된 규칙을 만들자고 해서 나온 것이 **REST API**이다. ([REST API 참고](https://blog.naver.com/ydot/222738115724))

- 단순하게 컴퓨팅 처리를 쉽게 해주는 기능으로 볼 수 있다.

### JSON(JavaScript Object Notation)

--- 

- **API**를 통해 데이터를 주고 받을 때 일정한 형식에 맞추지 않는다면 불편하기 때문에 만들어진 주로 사용되는 형식이다. 

- **JSON** viewer로 간단하게 볼 수 있다.

### CLI(Command Line Interface)

---

- 터미널을 통해 사용자와 컴퓨터가 상호 작용하는 방식

- *GUI(Graphic User Interface)* : 그래픽을 통해 사용자와 컴퓨터가 상호 작용하는 방식

- Interface란 서로 다른 개체끼리 맞닿아 있는 면을 본래 뜻한다. 여기에서는 사용자와 컴퓨터가 서로 소통하는 접점이라고 이해할 수 있겠다.

- GUI는 CLI에 비해 사용이 쉽지만 컴퓨터의 성능을 더 많이 소모한다. 그리고 CLI는 GUI로는 불가능한 많은 세부적인 기능을 사용할 수 있다.

- 절대경로 : 최초 디렉토리를 기준으로 경유한 경로를 모두 기입하는 방식
  ex) 'C:\Desktop\work\img\logo.jpg'

- 상대경로 : '현재 위치한 곳을 기준'으로 해서 '목적파일의 위치'이다.
  ex) '../img/logo.jpg'

### Markdown

- 텍스트 기반의 언어
- 쉽게 쓰고 읽고 하는데 도움이 되는 것
- html로 변환이 가능함.

### Git

working area 에서 Remote repo로 이동하는 과정은 아래와 같다.

1. working area 에서 git add 으로 staging area로 옮긴다.
2. staging area에서 commit하여 git directory로 옮긴다. (여기까지는 로컬 영역 즉, 내 컴퓨터 내에서 일어나는 일)
3. git directory(git area)에서 Push하여 Remote repo(원격저장소 Github)로 옮긴다.
4. Remote repo에서 working area로 옮기기 위해서는 pull이나 clone을 사용한다.

```git
git config --global user.name "이름"
git config --global user.email "메일주소"
git config --global -l
git init
git status
echo hello world! > a.txt
git add a.txt staging area로 올리기
git add *.txt 모든 txt파일
git . 현재 디렉토리 내 모든 파일
git reset -- a.txt unstaged로 내리기(동시에 원격저장소의 파일 삭제)
git rm --cached a.txt unstaged로 내리기(스테이징에서 파일만 내리기)
```
