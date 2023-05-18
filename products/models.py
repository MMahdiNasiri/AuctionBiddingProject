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
    name = models.CharField(max_length=50)
    description = models.TextField()
    seller = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False, blank=False)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(default=0)

    def __str__(self):
        return self.name

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
