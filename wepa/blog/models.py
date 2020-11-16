from django.db import models
from django.utils import timezone


class Tag(models.Model):

    name = models.CharField(max_length=20,
                            null=False)

    def __str__(self):
        return self.name


class Post(models.Model):

    headline = models.CharField(max_length=100, null=False)
    text = models.CharField(max_length=1000, null=False)
    date = models.DateTimeField(null=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.headline

    # todo: make method and add to admin.py 'list_display'
    def has_comments(self):
        pass


# ForeignKey.related_query_name¶
# https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.ForeignKey.related_query_name

class Comment(models.Model):
    text = models.CharField(max_length=500)
    author = models.CharField(max_length=40, default='anonymous')
    date = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments',
                             related_query_name='comment',)

    def __str__(self):
        return self.text


# posts = Post.objects.filter(comment__text__contains='song')
# get all posts with comments in which there is 'song'
