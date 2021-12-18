from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# polls/views 호출하기 위해 만든 이 urls.py파일을 다시 최상위 urlConf인 mysite/urls.py에 연결해줘야한다.