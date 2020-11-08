from django.db import models


class Task(models.Model):

    task_text = models.CharField(max_length=100)

    def __str__(self):
        return self.task_text



