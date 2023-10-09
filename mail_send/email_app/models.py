from django.db import models

# Create your models here.
class Employee(models.Model):
    event_choices =(
        ('birthday','Birthday'),
        ('anniversary','Anniversary')
    )
    name = models.CharField(max_length=100)
    email_id = models.EmailField()
    birth_date = models.DateField()
    event_type = models.CharField(choices=event_choices,max_length=20,default='birthday')




