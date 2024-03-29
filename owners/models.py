from django.db import models

# Create your models here.


class Owner(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=200)
    age = models.IntegerField(null=True)

    class Meta:
        db_table = 'owners'


class Dog(models.Model):
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    age = models.IntegerField(null=True)

    class Meta:
        db_table = 'dogs'

