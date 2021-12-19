from django.urls import path

from . import views

urlpatterns = [
    # 모든 팀 조회
    path('/teams', views.ListTeamView.as_view()),
    # 팀생성
    path('', views.TeamView.as_view()),
    #팀 등록
    path('/register', views.RegisterTeamView.as_view()),

    # 팀삭제
    path('/<int:team_id>', views.DeleteTeamView.as_view()),

    # 팀의 멤버 조회
    path('/members/<int:team_id>', views.MembersView.as_view())
]