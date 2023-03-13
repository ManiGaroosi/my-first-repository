from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateField()
    amount = models.BigIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)