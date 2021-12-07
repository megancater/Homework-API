from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import datetime

# Assignment model
class Assignment(models.Model):
    # Model attributes
    name = models.CharField(max_length=50)
    due_date = models.DateField()
    class_name = models.CharField(max_length=50)
    description = models.TextField()
    completed = models.BooleanField()

    # Returns assignnment id if string requested
    def __str__(self):
        return str(self.id)


class Timer(models.Model):
    # Timer attributes
    assignment = models.ForeignKey(
        'Assignment', on_delete=models.CASCADE, related_name='timers') # Deletes timer if assignment deleted
    begin = models.DateTimeField()
    end = models.DateTimeField()

    # Ensures timer start is before timer stop
    def clean(self):
        if self.begin > self.end:
            raise ValidationError('Begin should be before end')
        return super().clean()

    # Saves timer
    def save(self, *args, **kwargs):
        if self == "TimerForm":
            return super(Timer, self).save(*args, **kwargs)

        # If not set, timer start is set to current time
        if not self.begin:
            self.begin = timezone.now()

        # Timer stop is set to current time
        self.end = timezone.now()
        return super(Timer, self).save(*args, **kwargs)

    # Edits and saves time
    def edit(self, *args, **kwargs):
        return super(Timer, self).save(*args, **kwargs)

    # Returns timer id if string requested
    def __str__(self):
        return str(self.id)
