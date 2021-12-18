# Django 기본

- 파이썬 풀스택 프레임워크
- manage.py 를 통해서 여러 명령어를 실행할수있음
- `python manage.py runserver` : 개발서버 실행(파이썬으로만 실행되는 경량서버로 개발에서만 사용하도록! 배포할땐 nginx나 apache를 사용하자)

## 주요 파일들

- manage.py : 실행파일로 이 파일을 통해 여러가지 명령어를 실행할 수 있음(서버 실행..)
- settings.py : 프로젝트 전반의 환경설정
- urls.py : 요청오는 url과 매핑하는 작업을 함
- wsgi.py : 위스기라고 부르더라, 웹서버와 장고를 연결해주는 작업

## 프로젝트와 앱
- 앱들이 모여 프로젝트가 된다. 프로젝트는 여러 앱을 포함할 수 있음
- 앱은 모듈인듯 하다.(NestJS에서의 모듈과 같은 기능을 가진다 생각됨)

# Django와 DB

## 장고와 DB
- settings.py에서 데이터베이스 설정을 할수 있네..
- settings.py의 INSTALLED_APPS는 DB테이블을 사용하는데, 이 테이블은 미리 만들어야한다.`python manage.py migrate`를 통해서 테이블들을 만든다.
- (필요없는 INSTALLED_APPS)는 삭제하고 migrate명령어를 사용하자.

> migrate는 INSTALLED_APPS에 등록된 어플에만 한하여 실행됨!

## 모델만들기
- 모델은 테이블을 의미한다. (DB테이블과 매핑되는 엔티티 클래스가 더적절)
- models.py라고 이미 만들어진 (앱의 하위 파일) 곳에 모델 클래스를 작성하면 되네.

## 모델 만들었으니 모델 실제로 적용할 준비(활성화)
- 현재 프로젝트(mysite)에 polls앱이 설치된 것을 알려야한다. (장고는 프로젝트가 여러 앱을 가지고 있는 형태로 존재한다.(모듈들))
- 앱(polls)를 현재 프로젝트(mysite)에 포함시키려면 mysite의 settings.py의 INSTALLED_APPS에 polls를 추가해야한다.
- 어떻게? polls.apps.PollsConfig라는 설정 클래스를 추가하면 된다.

## manage.py를 통해 makemigrations 실행
- 데이터베이스에 테이블을 만들기 위한 설계도를 만드는 작업이다.
- 해당 명령어를 실행하면 앱의 migrations 파이썬 패키지 내에 뭔가 파일이 생기는데 그게 DB에 테이블 적용하기 위한 설계도이다! 

## manage.py를 통해 migrate명령어 실행
- makemigrations를 통해 만들어진 설계도를 토대로 실제로 디비에 테이블을 생성한다.

> dbEaver로 디비 확인해봤는데 테이블 잘 생성되었다. 그런데 내가 만들지 않은 테이블도 있던데? 그건 INSTALLED_APP의 어플리케이션이필요로하는 테이블 인듯 하다. 찾아봐서 필요없다 싶으면 ISNTALLED_APP에서 삭제하고 migrate명령어 실행해야 겠따

## Django shell
- django에서 제공하는 api를 이용할수있다.
- `./manage.py shell` 하면 쉘이 하나 뜬다. 해당 쉘에서 다양한 api를 실행할 수 있다. 
- 놀라운건 shell에서 api를 통해 db에 쿼리를 날릴 수 있다..(다양한 db작업을 여기서 할 수 있따.)