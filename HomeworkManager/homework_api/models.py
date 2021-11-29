from django.db import models

class Assignment(models.Model):
    name = models.CharField(max_length=50)
    due_date = models.DateField()
    class_name = models.CharField(max_length=50)
    description = models.TextField()
    completed = models.BooleanField()

    def __str__(self):
        return self.id

class Timer(models.Model):
    assignment = models.ForeignKey('Assignment', on_delete=models.CASCADE)
    begin = models.TimeField(auto_now_add=True)
    end = models.TimeField(auto_now=True)
