from django.shortcuts import render, HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import League, Athlete, nflStats, nbaStats, mlbStats
from .serializers import LeagueSerializer, AthleteSerializer, NFLStatsSerializer, NBAStatsSerializer, MLBStatsSerializer


# Create your views here.

def hello(request):
    return HttpResponse("Hello World")

class LeagueViewSet(viewsets.ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    # TODO: If we choose to have user-pw authentication system, replace "AllowAny" to "IsAuthenticated" (no quotation marks)
    #       Do this for all calls of permission_classes in views.py
    permission_classes = [AllowAny] 

# TODO: Create versions of view sets that displays less data (e.g. name only, basic stats, etc.)

class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    # Filter athletes by league
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['league'] #TODO: Figure out how to filter by league name rather than enum value
    # e.g. /api/athletes/?league=NFL rather than /api/athletes/?league=2
    
    # filterset_fields = ['league__league'] # this gives the behavior I want, however I don't want to have to query 
    # with /api/athletes/?league__league=NFL because it's ugly and convoltued, I want to be able to simply use
    # /api/athletes/?league=NFL
    permission_classes = [AllowAny]

class NFLStatsViewSet(viewsets.ModelViewSet):
    queryset = nflStats.objects.all()
    serializer_class = NFLStatsSerializer
    permission_classes = [AllowAny]

class NBAStatsViewSet(viewsets.ModelViewSet):
    queryset = nbaStats.objects.all()
    serializer_class = NBAStatsSerializer
    permission_classes = [AllowAny]