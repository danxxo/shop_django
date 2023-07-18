from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    is_consumer = models.BooleanField(default=True)

    def __str__(self):
        return f'Profile of {self.user.username}'
    