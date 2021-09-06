from django.db import models

class Password(models.Model):
    text = models.CharField(max_length=128)
