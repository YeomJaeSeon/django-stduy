# Django 기본

- 파이썬 풀스택 프레임워크
- manage.py 를 통해서 여러 명령어를 실행할수있음
- `python manage.py runserver` : 개발서버 실행(파이썬으로만 실행되는 경량서버로 개발에서만 사용하도록! 배포할땐 nginx나 apache를 사용하자, 개발용 서버답게 디버그 모드로 실행되네, 코드 수정하면 바로 reloading된다.)

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

## makemigrations로 생긴 설계도를 db에 적용시키기전 sql확인하기!
- `./manage.py sqlmigrate polls 0001`,  혹은 `0002`를 통해 실행될 sql을 출력하여 확인할 수 있다.

## manage.py를 통해 migrate명령어 실행
- makemigrations를 통해 만들어진 설계도를 토대로 실제로 디비에 테이블을 생성한다.

> dbEaver로 디비 확인해봤는데 테이블 잘 생성되었다. 그런데 내가 만들지 않은 테이블도 있던데? 그건 INSTALLED_APP의 어플리케이션이필요로하는 테이블 인듯 하다. 찾아봐서 필요없다 싶으면 ISNTALLED_APP에서 삭제하고 migrate명령어 실행해야 겠따

## Django shell
- django에서 제공하는 api를 이용할수있다.
- `./manage.py shell` 하면 쉘이 하나 뜬다. 해당 쉘에서 다양한 api를 실행할 수 있다. 
- 놀라운건 shell에서 api를 통해 db에 쿼리를 날릴 수 있다..(다양한 db작업을 여기서 할 수 있따.)

# Django와 관리자
- 장고에선 관리자 기능을 그냥 제공한다. 따로 admin페이지를 만드는 등의 작업을 하지 않아도된다!?!
- `./manage.py createsuperuser`명령어를 통해 관리자 생성가능
- 생성한뒤 개발 서버 실행 -> /admin 요청하면 내가 만들지 않은 페이지가 있을 거다. 이건 쟝고에서 제공하는 페이지, 관리자 기능!(스프링 시큐리티랑 비슷하다 생각했다.)
- 더 놀라운건 쟝고에서 제공하는 어드민 기능을 이용해서 django api를 이용할수 있따는 것이다.
  - shell에서 테스트한 api들을 그냥 gui로 클릭하니 db에 insert가 이루어진다.
- 내가 만든 모델을 admin에 추가하려면 
  - 내가 만든 앱 패키지의 `admin.py`에 아래와 같이 작성하면 된다.
```python
from django.contrib import admin
from polls.models import Question
# Register your models here.

# 내가 만든 모델을 어드민에 추가하는 코드
admin.site.register(Question)
```

# Django 뷰와 템플릿

## 뷰와 매핑되는 url중 pathVariable적용하기
- urls.py 에 `path('<int:question_id>/', views.detail, name='detail'),` 처럼 pathVariable을 적용할 수 있따. 추가로 name은 해당 url에 이름을 지정하는 것이다. 변수처럼 사용하여, 하드코딩을 막기 위한것.!
- 위 url의 pathVariable은 question_id라는 변수에 입력이된다.

## 쿼리날리기
- Question.objects. api를 통해서 쿼리를 날릴 수 있따. 이 부분은 보다더 정확한 쿼리를 위해 공부가 필요하다.

## 템플릿 엔진
- 스프링에선 jsp, thymeleaf와 같은 템플릿 엔진들을 사용했다. Django는 앱 패키지 아래 templates라는 패키지를 만들면 장고가 템플릿임을 인식한다. 
- context라는 것을 통해 view에서 데이터를 넣어 템플릿으로 전달한다. 스프링의 model과 같은 역할을 한다고 생각한다. (mvc의 model)

## 404 응답
- django.http로부터 Http404를 응답할 수  있다. 

## shortcut
- django.shortcut으로 부터 코드를 확 줄이게 도와주는 api들을 제공한다.
- `from django.shortcuts import render, get_object_or_404`

## url export하기(앱의 url namespace를 지정하는 방법 'app_name=namespace')
- polls.urls.py에서 name에 어떠한 문자열을 입력했었다. 이 문자열은 해당 url의 이름이라 했었다.
- 이 이름을 외부에서 사용할수 있도록 export할수 있다.
- app_name=polls와 같이 변수를 하나 생성하여 외부에서 접근할수 있도록 하면 된다.! 
- template에서는 하드코딩된 url말고 해당 변수 url 을 이용하면 더 쉬울것

# 클래스 뷰와, 지네릭 뷰
- 지금까진 함수형 뷰로 컨트롤러처리를 하였다. 클래스뷰를 바꾸면 코드를 깔끔하게 할 수있다.
- 클래스 뷰를 사용한 다는 것은 쟝고의 지네릭 뷰를 상속받아 해당 필드나 메서드르를 오버라이딩 해서 사용한다는 것이다. 즉, 추상화가 되어있어 나같이 쟝고 초보는 바로 적용하기가 힘들다 느낌.. 좀 더 많이 알아봐야 사용할거같다.(많이 적용해보고)
- 지네릭 뷰는 쟝고에서 제공하는 클래스들이다. 이 클래스를 상속받아 코드를 재사용하며 깔끔하게 할수 있다.. 
- urlConf에서 클래스뷰를 사용하면 as_view()메서드를 이용해야 한다.
- 그다음 폼을 통해 post요청하는 것에 대한 처리를 한번 해보았다. 딱히 어려운건 없었다. 그러나 csrf같은 보안도 쟝고에서 제공해준다는 것이 좋았다. 뭔가 간단하고 가벼운 프레임워크인줄 알았는데 정말 다양한것을 제공해주는 것 같다 느꼈다. 꽤 무거운 프레임워크가 아닐까? 파이썬 언어 자체도 인터프리터로 느린 언어인데, 이런 생각이들었다.