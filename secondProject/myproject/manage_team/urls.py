from django.urls import path

from . import views

urlpatterns = [
    path('', views.create_team),
    path('/<int:team_id>', views.delete_team),
    path('/register', views.register_team),
    path('/members/<int:team_id>', views.find_members_by_team_id)
]