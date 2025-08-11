from django.db import models

# Create your models here.

# TODO: Create choices for positions (and teams?)
# TODO: Have choices affect stats (e.g. if pos is QB then display passing stats)

class Sport(models.TextChoices):
    NFL = 'NFL'
    MLB = 'MLB'
    NBA = 'NBA'

class Athlete(models.Model):
    name = models.CharField(max_length=200)
    sport = models.CharField(
        max_length=3,
        choices=Sport.choices,
        default=Sport.NFL
    )