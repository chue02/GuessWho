from rest_framework import serializers
from .models import League, Athlete, nflStats, nbaStats, mlbStats


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'
        extra_kwgs = {'league' : {'read_only': True}}

        
class NFLStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = nflStats
        fields = '__all__'

class NBAStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = nbaStats
        fields = '__all__'

class MLBStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = mlbStats
        fields = '__all__'


class AthleteSerializer(serializers.ModelSerializer):
    # By placing stats serializers in the athlete serializer,
    # whenever you serialize an athlete you'll get their stats
    # nested inside.
    # NOTE: If you want to update an athlete's stats, remove read_only
    nflStats = NFLStatsSerializer(read_only=True)
    nbaStats = NBAStatsSerializer(read_only=True)
    mlbStats = MLBStatsSerializer(read_only=True)


    class Meta:
        model = Athlete
        fields = '__all__'
        # extra_kwgs = {'name' : {'read_only': True}}