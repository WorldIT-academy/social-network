from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='images/avatars',null=True, blank=True)
    date_of_birth = models.DateField()
    friends = models.ManyToManyField("self", symmetrical=True, blank=True)

    def __str__(self):
        return self.user.username
