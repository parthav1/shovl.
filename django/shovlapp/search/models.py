from django.db import models
from django.contrib.auth.models import User

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_id = models.IntegerField()
    company_name = models.TextField()
    description = models.TextField()
    min_project_size = models.TextField()
    employees = models.TextField()
    founded = models.TextField()
    located = models.TextField()
    rating = models.FloatField()
    reviews = models.JSONField()
    clients = models.TextField()
    notable_projects = models.TextField()
    ranking = models.IntegerField()
    shovl_score = models.FloatField()
    website = models.TextField()
    hourly_rate = models.TextField()
    review_count = models.IntegerField()
    sentiment_score = models.FloatField()
    stars = models.IntegerField()
