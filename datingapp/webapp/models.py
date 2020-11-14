from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='booked')

class Booktickets(models.Model):
    sex_choice=(('male','Male'),('female','Female'),('other','Other'))
    occassion_choice=(('birthday','Birthday'),('marriage','Marriage'),('holiday','Holiday'),('meeting','Meeting'))
    #STATUS_CHOICES=(('booked','Booked'),('cancelled','Cancelled'))
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    sex=models.CharField(max_length=7,choices=sex_choice,default='male')
    email=models.EmailField()
    address=models.CharField(max_length=200)
    tickets=models.IntegerField()
    date=models.DateField(blank=False)
    adults=models.IntegerField()
    children=models.IntegerField(blank=True,null=True)
    occassion=models.CharField(max_length=20,choices=occassion_choice,default='holiday')
    ordered=models.DateTimeField(auto_now_add=True)
    #status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='booked')

    class Meta:
        ordering=('-ordered',)

    def __str__(self):
        return self.name



    def get_absolute_url(self):
        return reverse('list',kwargs={'id':self.id})



    #def pricing(self):
    #    if occassion_choice=="birthday":
    #        price=50000
    #    elif occassion_choice=="marriage":
    #        price=1000000
    #    elif occassion_choice=="holiday":
    #        price=(adult*3000)+(child*2000)
    #    elif occassion_choice=="meeting":
    #        price=40000
    #    return self.price
