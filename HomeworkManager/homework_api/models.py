from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import datetime


class Assignment(models.Model):
    name = models.CharField(max_length=50)
    due_date = models.DateField()
    class_name = models.CharField(max_length=50)
    description = models.TextField()
    completed = models.BooleanField()

    def __str__(self):
        return str(self.id)


class Timer(models.Model):
    assignment = models.ForeignKey(
        'Assignment', on_delete=models.CASCADE, related_name='timers')
    begin = models.DateTimeField()
    end = models.DateTimeField()

    def clean(self):
        if self.begin > self.end:
            raise ValidationError('Begin should be before end')
        return super().clean()

    def save(self, *args, **kwargs):
        if self == "TimerForm":
            return super(Timer, self).save(*args, **kwargs)

        if not self.begin:
            self.begin = timezone.now()
        self.end = timezone.now()
        return super(Timer, self).save(*args, **kwargs)

    def edit(self, *args, **kwargs):
        return super(Timer, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)
