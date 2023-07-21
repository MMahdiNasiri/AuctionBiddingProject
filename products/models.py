from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from AuctionBidding.baseModels import BaseModel


class Category(BaseModel):
    logo = models.ImageField(upload_to='logo')
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['parent', ]),
            models.Index(fields=['name', ])
        ]

    def __str__(self):
        return self.name


class Products(BaseModel):
    INIT = 'init'
    STOCK = "stock"
    SOLD = "sold"
    BIDDING = "bidding"
    PRODUCT_STATUS_CHOICES = [
        (INIT, "Init"),
        (STOCK, "Stock"),
        (SOLD, "Sold"),
        (BIDDING, "Bidding"),
    ]

    name = models.CharField(max_length=50)
    description = models.TextField()
    seller = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=False, blank=False,
                                 related_name='products')
    base_price = models.IntegerField()
    status = models.CharField(
        max_length=10,
        choices=PRODUCT_STATUS_CHOICES,
        default=INIT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    def is_editable(self):
        return self.status in {self.INIT, self.STOCK}

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"slug": self.identifier})

    class Meta:
        indexes = [
            models.Index(fields=['name', 'deleted', ]),
            models.Index(fields=['category', 'deleted']),
            models.Index(fields=['seller', 'deleted']),
        ]


class ProductPictures(models.Model):
    picture = models.ImageField(upload_to='products')
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING, null=False, blank=False, related_name='pictures')

    class Meta:
        indexes = [
            models.Index(fields=['product', ]),
        ]

    def __str__(self):
        return self.__str__() + self.product
