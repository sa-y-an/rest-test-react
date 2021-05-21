from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, URLField
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=1000)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)