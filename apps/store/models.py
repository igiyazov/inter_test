from django.db import models
import hashlib

from hashsite.mixins import HashFieldMixin

class Consumer(HashFieldMixin):
    name = models.CharField(
        'Company name',
        max_length=250,
    )
    phone = models.CharField(
        'Phone number',
        max_length=10,
    )
    founder = models.CharField(
        'Founder of company',
        max_length=200,
    )

    def save(self, *args, **kwargs):
        self.hash = hashlib.md5(bytes(self.name, encoding='utf-8')).hexdigest()
        super().save(*args, **kwargs)




class Store(HashFieldMixin):
    name = models.CharField(
        'Store name',
        max_length=250,
    )
    phone = models.CharField(
        'Phone number',
        max_length=10,
    )
    address = models.CharField(
        'Store address',
        max_length=300,
    )

    def save(self, *args, **kwargs):
        self.hash = hashlib.md5(bytes(self.name, encoding='utf-8')).hexdigest()
        super().save(*args, **kwargs)
