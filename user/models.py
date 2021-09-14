import hashlib
import random
from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class User(AbstractUser):
    image = models.ImageField(upload_to='user_images', blank=True, null=True)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

    def is_activation_key_expires(self):
        return now() <= self.activation_key_expires

    def generate_activation_key(self):
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        self.activation_key = hashlib.sha1((self.email + salt).encode('utf8')).hexdigest()
        self.activation_key_expires = now() + timedelta(hours=48)
        return None

