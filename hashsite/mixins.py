from django.db import models

class HashFieldMixin(models.Model):
    hash = models.CharField(
        'Hash field', 
        max_length=16,
        blank=False,
        db_index=True,
    )

    class Meta:
        abstract = True
    

    @classmethod
    def search_by_hash(cls, hash):
        return cls.objects.filter(
            hash__icontains=hash,
        ).values('id')