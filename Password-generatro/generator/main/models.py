from django.db import models

# Create your models here.

class PasswordConfiguration(models.Model):
    length = models.PositiveIntegerField(default=8)
    include_uppercase = models.BooleanField(default=True)
    include_lowercase = models.BooleanField(default=True)
    include_numbers = models.BooleanField(default=True)
    include_special = models.BooleanField(default=True)

    def __str__(self):
        return f"Config: {self.length} characters"
