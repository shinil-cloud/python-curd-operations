from django.db import models

# Create your models here.

"""name,email,ph,date,gender,experience,hospitalname,state,district,address"""
class Ert(models.Model):
    gen=(
        ('male','Male'),
        ('female','Female'),
        )
    name=models.CharField(max_length=100,unique=True,
    error_messages={
        "unique":"This name already exist"
    }
    )
    email=models.EmailField()
    ph=models.IntegerField()
    date=models.DateTimeField()
    experience=models.IntegerField(default=0)
    hospitalname=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    gender=models.CharField(max_length=10,choices=gen)
    
    def __str__(self):
        return self.name