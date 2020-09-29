from django.db import models

# Create your models here.
class Emails(models.Model):
    email = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.email}"


