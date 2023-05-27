from django.db import models
from django.utils import timezone
from django.utils.text import slugify
import hashlib


class BaseModel(models.Model):
    name = models.CharField(max_length=30)
    deleted = models.IntegerField(default=0)
    identifier = models.SlugField(unique=True, max_length=12, allow_unicode=True, blank=True)

    class Meta:
        abstract = True

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.identifier:
            slug = f'{self.name}{timezone.now()}'
            self.identifier = slugify(hashlib.blake2b(slug.encode(), digest_size=6).hexdigest())
        super(BaseModel, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def delete(self, using=None, keep_parents=False):
        self.deleted = self.id
        self.save()
