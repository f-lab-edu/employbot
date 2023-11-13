<center>
<img src="https://github.com/f-lab-edu/employbot/assets/55238671/45e8bb0b-7a2f-4c0d-a940-a88622635c24" width=600>
</center>

# Slack API를 이용한 취업봇 만들기
취업봇은 개발하는 개발자분들이 자주 이용하는 Slack 채널에서 취업 및 이직 준비를 빠르고 쉽게 도와드리기 위해 만들어진 봇입니다.
취업봇을 통해 구직 정보를 빠르게 찾아볼 수 있습니다.

## 💻 기술 스택
- Python 3.9
- FAST API
- Slack API
- AWS EC2, Nginx

## ⚒️ 기능
- 잡코리아, 사람인, 원티드, 인디드 등의 구직 사이트 검색 기능 및 포지션 검색 기능
- AWS EC2와 Nginx를 이용한 무중단 배포 서버 구현

### 구직 검색
<center>
<img src="https://user-images.githubusercontent.com/55238671/277393027-d771b39d-0dfc-4ac3-b1fb-d4a569a868c5.gif" width=300>
</center>


- 세부적인 포지션을 이용해 검색하는 방법과 간단한 통합 검색으로 다양한 취업 정보 사이트 URL를 연결해주는 기능이 있습니다.
- 취업 관련 정보를 Slack API를 통해 시각적으로 나타냅니다. 추후 일정을 등록하여 편리하게 관리할 수 있습니다.

### 배포
<center>
<img src="https://user-images.githubusercontent.com/55238671/277400188-6333c9a1-0088-4b00-8be6-93a804f0d7c9.png" width=500>
</center>

- AWS EC2 서버 내에서 Ngnix를 이용하여 Public IP와 연결하였습니다.
- 세션이 종료되도 실행할 수 있도록 `nohup`과 `&(백그라운드 실행)` 리눅스 명령어를 사용하였습니다.



## 👨‍💻 피드백
### 후기
제가 만든 SlackBot은 완전한 Public 상태까지는 구현하지 못했습니다. 이유는 Slack 자체에서 Free Plan에 대한 제약이 있었기 때문입니다. 원래는 SlackBot이 존재하는 채널을 통해 소통을 하거나 Direct Message의 Id를 받아 적용시킬려 했으나 Enterprise 버전에서만 가능하다고 합니다.

이번 프로젝트를 통해 지금까지 배워두었던 Django, Flask 웹 프레임워크에 비해 간결하게 코드를 작성할 수 있었고 이 덕분에 중복된 코드를 제거하거나 함수를 재구성하는 등 리팩터링이 비교적 쉬웠던 것 같습니다. 또한 비동기처리를 할 수 있는 FastAPI 덕분에 Slack API를 활용해도 빠른 속도로 구현해 낼 수 있었던 것 같습니다. (앞 그림은 GIF 파일 속도가 느린 것이기 때문에 양해부탁드립니다.ㅎㅎㅎ)


### 업데이트 예정
- 추후 S3에 데이터를 저장할 수 있는 일정 및 이력서 저장 기능을 구현할 예정입니다.
- 명령어 팁 기능을 사용하여 사용자의 입력어를 사용하여 해당 커맨드를 호출할 수 있는 기능를 구현할 예정입니다.


## 📝 개발 일지
<table>
  <tr>
    <th scope="col">순서</td>
    <th scope="col">내용</td>
  </tr>
  <tr>
    <td>1</td>
    <td><a href="https://velog.io/@dongwookang/Slack-취업-봇-만들기-EP01">취업봇 만들기 EP1</a></td>
  </tr>
  <tr>
    <td>2</td>
    <td><a href="https://velog.io/@dongwookang/Slack-취업-봇-만들기-EP02">취업봇 만들기 EP2</a></td>
  </tr>
    <tr>
    <td>3</td>
    <td><a href="https://velog.io/@dongwookang/Slack-취업-봇-만들기-EP03">취업봇 만들기 EP3</a></td>
  </tr>
    <tr>
    <td>4</td>
    <td><a href="https://velog.io/@dongwookang/Slack-취업-봇-만들기-EP04">취업봇 만들기 EP4</a></td>
  </tr>
    <tr>
    <td>5</td>
    <td><a href="https://velog.io/@dongwookang/Slack-취업-봇-만들기-EP05">취업봇 만들기 EP5</a></td>
  </tr>
</table>
