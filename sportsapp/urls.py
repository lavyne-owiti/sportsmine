from django.urls import path
from . import views

app_name='sportsapp'
urlpatterns = [

    path('',views.home, name="home"),
    path('list_player/',views.list_player,name='list_player'),
    path('coach_list/',views.coach_list,name='coach_list'),
    path('referee_list/',views.referee_list,name='referee_list'),
    path('leader_list/',views.leader_list,name='leader_list'),
    path('news_feed/',views.news_feed,name='news_feed'),
    path('fixture_list/',views.fixture_list,name='fixture_list'),
    path('award_list/',views.award_list,name='award_list'),
    path('match_ofthe_day/',views.match_ofthe_day,name='match_ofthe_day'),
    path('team/',views.team,name='team'),
    path('contact/',views.contact,name="contact"),
    
]
