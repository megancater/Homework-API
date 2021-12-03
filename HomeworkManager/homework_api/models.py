from django.db import models
from django.utils import timezone
from datetime import datetime


class Assignment(models.Model):
    name = models.CharField(max_length=50)
    due_date = models.DateField()
    class_name = models.CharField(max_length=50)
    description = models.TextField()
    completed = models.BooleanField()

    def __str__(self):
        return self.id


class Timer(models.Model):
    assignment = models.ForeignKey(
        'Assignment', on_delete=models.CASCADE, related_name='timers')
    begin = models.DateTimeField()
    end = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.begin:
            self.begin = timezone.now()
        self.end = timezone.now()
        return super(Timer, self).save(*args, **kwargs)
