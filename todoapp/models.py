from django.db import models
from django.contrib.auth.models import User

class TodoItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task