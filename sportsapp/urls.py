from django.urls import path
from sportsapp.views import start

urlpatterns = [
    path('start/', start,name="start"),
]
