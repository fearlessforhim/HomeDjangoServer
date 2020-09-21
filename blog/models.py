import uuid
from django.db import models


# Create your models here.

class BlogPost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField('Post Title', max_length=75)
    content = models.TextField('Post Content')
    dateCreated = models.DateTimeField('Date Created', auto_now_add=True)
    lastUpdated = models.DateTimeField('Last Updated', auto_now=True)
    datePublished = models.DateTimeField('Date Published', null=True, blank=True)


class AboutMePost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField('Post Content')
    lastUpdated = models.DateTimeField('Last Updated', auto_now=True)
