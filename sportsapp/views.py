from django.shortcuts import render

from sportsapp.models import Award, Coach, Fixture, Leader, Match, New_report, Player, Referee, Team

# Create your views here.
def home(request):
    """the home page for sports"""
    return render(request,'sportsapp/home.html')
def contact(request):
    return render(request,'sportsapp/contact.html')

def list_player(request):
    players=Player.objects.all()
    return render(request,'sportsapp/player.html',{'players':players})

def coach_list(request):
    coaches=Coach.objects.all()
    return render (request,'sportsapp/coach.html',{'coaches':coaches})

def referee_list(request):
    referees=Referee.objects.all()
    return render (request,'sportsapp/referee.html',{'referees':referees})

def leader_list(request):
    leaders=Leader.objects.all()
    return render(request,'sportsapp/referee.html',{'leaders':leaders})

def news_feed(request):
    feeds=New_report.objects.all()
    return render(request,'sportsapp/news_feeds.html',{'feeds':feeds})

def fixture_list(request):
    fixtures=Fixture.objects.all()
    return render(request,'sportsapp/fixtures.html',{'fixtures':fixtures})

def award_list(request):
    awards=Award.objects.all()
    return render(request,'sportsapp/awards.html',{'awards':awards})

def match_ofthe_day(request):
    matches=Match.objects.all()
    return render(request,'sportsapp/match.html',{'matches':matches})

def team(request):
    teams=Team.objects.all()
    return render(request,'sportsapp/teams.html',{'teams':teams})