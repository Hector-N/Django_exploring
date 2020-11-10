import random

from django.db import models
from django.utils import timezone




class Joke(models.Model):

    joke_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published', default=timezone.now())
    author = models.CharField(max_length=30)

    @classmethod
    def random_joke(cls):
        jokes = cls.objects.all()
        random_joke = random.choice(jokes)
        return random_joke

    def __str__(self):
        return f"{self.joke_text}\n" \
               f"\t\t\t{self.author}"






