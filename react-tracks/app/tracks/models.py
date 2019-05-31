from django.db import models

# Create your models here. These will end up being turned into DB tables by Django.
# models.Model is a helper class that allows us to build a new database model
class Track(models.Model):
    # an ID field is added automatically.
    title = models.CharField(max_length = 50)

    # blank = True allows the value to not be provided (null value in DB)
    description = models.TextField(blank = True)
    url = models.URLField()

    # auto_now_add allows for automatically populating new records with the current time.
    created_at = models.DateTimeField(auto_now_add=True)