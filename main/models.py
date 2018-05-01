from django.db import models
from random import choice
from string import ascii_letters
from django.utils import timezone

CHAR_NUMB = 12

def generig_passwd():
    return ''.join(choice(ascii_letters) for i in range(CHAR_NUMB))


class Login(models.Model):
    passwd = models.CharField(max_length=20, default=generig_passwd())

    def __str__(self):
        return self.passwd


class Records(models.Model):
    name_team = models.CharField(max_length=30)
    dt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name_team
