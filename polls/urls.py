from django.urls import path

from . import views

app_name = 'polls' # 다른 앱에서도 해당 url을 사용할수 있도록, app_name을 지정해준다. 그러면 사용하는데선 'polls:detail'로 사용할 수 있다.
urlpatterns = [
    # /polls
    path('', views.index, name='index'),
    # /polls/5
    path('<int:question_id>/', views.detail, name='detail'),
    # /polls/5/results
    path('<int:question_id>/results', views.results, name='results'),
    # /polls/5/vote
    path('<int:question_id>/vote', views.vote, name='vote')
]

# polls/views 호출하기 위해 만든 이 urls.py파일을 다시 최상위 urlConf인 mysite/urls.py에 연결해줘야한다.