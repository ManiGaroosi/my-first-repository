from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateField()
    amount = models.BigIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.BigIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text 