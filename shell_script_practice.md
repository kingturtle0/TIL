```bash
touch text.txt    (빈파일 생성)
mkdir folder    (디렉터리 생성)
ls -a    (-a : all 옵션. 숨김 파일까지 모두 보여줍니다)
mv text.txt folder     (text.txt를 folder 폴더 안에 넣을 때)
touch text1.txt    (빈파일 생성)
mv text1.txt text2.txt     (text1.txt의 이름을 text2.txt로 바꿀 때)
mkdir folder2
mv folder2 folder
cd folder
cd ..    (부모 디렉터리로 이동) (띄어쓰기 주의)
cd -    (바로 이전 디렉터리로 이동) (띄어쓰기)
start text.txt    (파일 여는데 mac에서는 start 대신 open)
rm text2.txt    (파일삭제)
rm -r folder    (디렉토리 삭제)

파이썬에서 가상환경을 통해서 개발을 하는것을 알아보자
가상환경은 쉽게 이야기 하자면 프로젝트 별로 package를 따로 관리 하는 것
cd pt1    
python -m venv turtle가상환경이름         <가상환경 만들기>
source turtle/Scripts/activate    <가상환경 활성화>
pip install numpy         <넘파이 패키지 설치해보기>
deactivate        <가상환경 비활성화>

git init
git remote add 이름(origin) 주소(https://~~)
git add .
git commit -m "~~~"
git push origin master
```
