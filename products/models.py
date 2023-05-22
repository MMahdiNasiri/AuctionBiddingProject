import hashlib

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='logo')

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='logo')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=False, blank=False)

    class Meta:
        indexes = [
            models.Index(fields=['category', ]),
            models.Index(fields=['name', ])
        ]

    def __str__(self):
        return self.name


class Products(models.Model):
    INIT = 'init'
    STOCK = "stock"
    SOLD = "sold"
    DELIVERED = "delivered"
    PRODUCT_STATUS_CHOICES = [
        (INIT, "Init"),
        (STOCK, "Stock"),
        (SOLD, "Sold"),
        (DELIVERED, "Delivered"),
    ]

    name = models.CharField(max_length=50)
    description = models.TextField()
    seller = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False, blank=False)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING, null=False, blank=False)
    status = models.CharField(
        max_length=10,
        choices=PRODUCT_STATUS_CHOICES,
        default=INIT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(default=0)
    hashId = models.CharField(max_length=12)

    def __str__(self):
        return self.name

    def editable(self):
        return self.status in {self.INIT, self.STOCK}

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):

        super(Products, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

        if not self.hashId:
            self.hashId = hashlib.blake2b(repr(self.id).encode(), digest_size=6).hexdigest()
            super(Products, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    class Meta:
        indexes = [
            models.Index(fields=['name', 'deleted', ]),
            models.Index(fields=['sub_category', 'deleted']),
            models.Index(fields=['seller', 'deleted']),
        ]


class ProductPictures(models.Model):
    picture = models.ImageField(upload_to='products')
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING, null=False, blank=False)

    class Meta:
        indexes = [
            models.Index(fields=['product', ]),
        ]

    def __str__(self):
        return self.__str__() + self.product
