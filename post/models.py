from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 100)
    date_created = models.DateTimeField(default=datetime.now)
    date_updated = models.DateTimeField(default=datetime.now)
    content = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'Post: {}'.format(self.title)

class Comment(models.Model):
    date_created = models.DateTimeField(default=datetime.now)
    comment = models.CharField(max_length = 200)
    content = models.TextField()
    post = models.ForeignKey(Post,
                on_delete = models.CASCADE,
                related_name = 'comments',
                null=True, blank=True)

    def __str__(self):
        return 'Comment {}'.format(self.comment)
