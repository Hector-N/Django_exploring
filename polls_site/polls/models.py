from django.db import models

class Question(models.Model):

    text = models.CharField(max_length=300)
    date = models.DateTimeField()

    def __str__(self):

        return self.text


class Option(models.Model):
    text = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):

        return self.text
