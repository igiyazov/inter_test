import hashlib
from django.contrib.auth.models import AbstractUser

from hashsite.mixins import HashFieldMixin

class BaseUser(AbstractUser, HashFieldMixin):
    
    def save(self, *args, **kwargs):
        self.hash = hashlib.md5(bytes(self.username, encoding='utf-8')).hexdigest()
        super().save(*args, **kwargs)