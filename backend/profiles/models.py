from django.contrib.auth.models import User
from django.db import models

from AuctionBidding.baseModels import BaseModel


# Create your models here.

class Profile(BaseModel):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile')
    name = models.CharField(max_length=30, blank=True)
    credit = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.name is None:
            self.name = self.user.username
        super(Profile, self).save(force_insert=False, force_update=False, using=None, update_fields=None)
