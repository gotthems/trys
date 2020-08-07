from django.db import models
import datetime


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=500, unique=True)
    content = models.TextField()
    created_time = models.DateTimeField(auto_created=True, auto_now_add=True)


    def __str__(self):
        return self.title
