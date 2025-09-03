from django.db import models
from django.forms import ValidationError
import datetime

# Create your models here.

class League(models.Model):
    class LeagueChoices(models.TextChoices):
        noLeague = "No League"
        NFL = "NFL", "nfl"
        NBA = "NBA", "nba"
        MLB = "MLB", "mlb"


    league = models.CharField(max_length=50, choices=LeagueChoices.choices, unique=True, default=LeagueChoices.noLeague)

    def __str__(self):
        return self.league

def get_default_league():
    league, created = League.objects.get_or_create(
        league=League.LeagueChoices.noLeague
    )
    return league.id

# TODO: the following fields
# Yrs active, age, DoB ...
class Athlete(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="athletes", default=get_default_league)
    name = models.CharField(max_length=200, default="Unnamed Athlete", unique=True) 
    position = models.CharField(max_length=10, default="")
    teams = models.CharField(max_length=100, default="")
    birthdate = models.DateField(default=datetime.date(1500, 1, 1))

    college = models.CharField(max_length=300, default="No College") # stores multiple colleges as one string (e.g. for Dillon Gabriel: Central Florida, Oklahoma, Oregon)
    draft = models.CharField(max_length=300, default = "Undrafted")
    active = models.BooleanField(default = True) # is player retired or not?

    awards = models.CharField(max_length=1000, default="") # fits all accolades into one huge string

    # TODO: add default image to this field
    # headshot = models.ImageField()

    def __str__(self):
        return self.name


# NOTE: All stats will be final career stats

class nflStats(models.Model):
    # Universal info and stats
    athlete = models.OneToOneField(Athlete, on_delete=models.CASCADE, related_name="nfl_stats")
    fumbles = models.IntegerField(default=0)

    # QB stats
    pass_yds = models.IntegerField(default=0)
    pass_tds = models.IntegerField(default=0)
    pass_ints = models.IntegerField(default=0)
    pass_rtg = models.FloatField(default=0.0)
    qb_rec = models.CharField(max_length=10)
    pass_sks = models.IntegerField(default=0)

    pass_cmps = models.IntegerField(default=0)
    pass_atts = models.IntegerField(default=0)
    pass_cmp_pct = models.FloatField(default=0.0)
    pass_yds_per_att = models.FloatField(default=0.0)

    # RB Stats
    rush_yds = models.IntegerField(default=0)
    rush_tds = models.IntegerField(default=0)
    rush_atts = models.IntegerField(default=0)
    rush_yds_per_att = models.FloatField(default=0.0)

    # WR/TE Stats
    rec_yds = models.IntegerField(default=0)
    rec_tds = models.IntegerField(default=0)
    recs = models.IntegerField(default=0)
    rec_yds_per_att = models.FloatField(default=0)

    # Defensive Stats
    # Tackles (NOTE: Tackles did not become a stat until 1994)
    solo_tkls = models.IntegerField(default=0)
    comb_tkls = models.IntegerField(default=0)
    def_sks = models.FloatField(default=0.0)
    tfl = models.IntegerField(default=0.0)

    # Turnovers
    ffmbls = models.IntegerField(default=0) # forced fumbles
    fmbl_tds = models.IntegerField(default=0)
    def_ints = models.IntegerField(default=0)
    def_int_tds = models.IntegerField(default=0)

    # TODO: Special Team stats
    
    def clean(self):
        league_value = getattr(self.athlete.league, "league", None)
        if league_value!= League.LeagueChoices.NFL:
            raise ValidationError(f"{self.athlete.name} is not in the NFL.")
        
    def save(self, *args, **kwargs):
        self.clean()  # enforce check on save
        super().save(*args, **kwargs)

# TODO: complete NBA stats
class nbaStats(models.Model):
    athlete = models.OneToOneField(Athlete, on_delete=models.CASCADE, related_name="nba_stats")
    points_per_game = models.FloatField()
    assists_per_game = models.FloatField()
    rebounds_per_game = models.FloatField()

    def clean(self):
        league_value = getattr(self.athlete.league, "league", None)
        if league_value != League.LeagueChoices.NBA:
            raise ValidationError(f"{self.athlete.name} is not in the NBA.")

    def save(self, *args, **kwargs):
        self.clean()  # enforce check on save
        super().save(*args, **kwargs)

# TODO: complete MLB stats
class mlbStats(models.Model):
    athlete = models.OneToOneField(Athlete, on_delete=models.CASCADE, related_name="mlb_stats")
    games = models.IntegerField(default=0)

    # Hitting counting stats
    plate_app = models.IntegerField(default=0)
    at_bats = models.IntegerField(default=0)
    hits = models.IntegerField(default=0)
    rbis = models.IntegerField(default=0)
    hrs = models.IntegerField(default=0)
    bb = models.IntegerField(default=0)
    sb = models.IntegerField(default=0)
    tb = models.IntegerField(default=0)
    ks = models.IntegerField(default=0.0)
    b_war = models.FloatField(default=0.0)

    # Hitting average stats
    batting_avg = models.FloatField(default=0.000)
    on_base_pct = models.FloatField(default=0.000)
    slg = models.FloatField(default=0.000)
    ops = models.FloatField(default=0.000)

    # Pitching stats
    ip = models.FloatField(default=0.0)
    era = models.FloatField(default=0.0)
    whip = models.FloatField(default=0.0)

    so = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    saves = models.IntegerField(default=0)


    def clean(self):
        league_value = getattr(self.athlete.league, "league", None)
        if league_value != League.LeagueChoices.MLB:
            raise ValidationError(f"{self.athlete.name} is not in the MLB.")

    def save(self, *args, **kwargs):
        self.clean()  # enforce check on save
        super().save(*args, **kwargs)


# TODO: Find way to display stats based on position (e.g. if position is QB display passing stats, if RB display rushing stats, if DL display tackles, etc.)
# TODO: Find way to display team names based on abbreviation (e.g. NYG=New York Giants, OAK=Oakland Raiders, LVR = Las Vegas Raiders)

