from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import LeagueViewSet, AthleteViewSet, NFLStatsViewSet, NBAStatsViewSet



router = DefaultRouter()
router.register(r'league', LeagueViewSet)
router.register(r'athlete', AthleteViewSet, basename='athlete')
router.register(r'nflStats', NFLStatsViewSet)
router.register(r'nbaStats', NBAStatsViewSet)


urlpatterns = [
    path("world", views.hello), # TODO: after creating paths with games views, delete this line.
    path('', include(router.urls)),
]
