from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

class CustomUser(AbstractUser):
    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)