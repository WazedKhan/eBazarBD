from sellers.models import Seller
from django.conf import settings
from django.utils import timezone
from django.db import models

from PIL import Image



class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_category')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sub_Category"
        verbose_name_plural = "Sub_Categories"




class Brand(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    discount = models.FloatField()
    image = models.ImageField(upload_to = 'products', blank = True, null = True)
    sub_cate = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Seller, on_delete=models.CASCADE)

    visited = models.IntegerField(default = 0)
    last_visit = models.DateTimeField(auto_now=True)
    total_sold = models.IntegerField(default=0)
    total_returned = models.IntegerField(default=0)
    refundable = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def total_earning(self):
        return self.total_sold * self.price

    def countVisitor(self):
        self.visited += 1
        self.save()

    def totalSold(self, quantity):
        self.total_sold += quantity
        self.save()

    def totalReturned(self):
        self.total_returned += 1
        self.save()

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
