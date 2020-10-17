from django.db import models
from django.contrib import auth
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    com_name = models.CharField(max_length=200)
    total_price = models.FloatField()
    quantity = models.PositiveIntegerField()
    # total_price = models.FloatField(default=0)
  
    UNIT_CHOICES = [
        ('kg', 'kilogram'),
        ('gm', 'gram'),
        ('nm', 'Number')
    ]
    
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default='gm')
    # unit = models.CharField(max_length=128)
    create_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("basic_app:detail", kwargs = {'pk': self.pk})

    def __str__(self):
        return self.com_name


class People(models.Model):
    name = models.CharField(max_length=200)
    total_bill = models.FloatField(default=0) 
    paid_money = models.FloatField(default=0)   # paid amount
    rem_money = models.FloatField(default=0)  # balance amount
    item_name = models.CharField(max_length=150)
    date = models.DateTimeField(default=timezone.now)
     
    def get_absolute_url(self):
        return reverse("basic_app:people_detail", kwargs = {'pk': self.pk})

    def __str__(self):
        return self.name





