from django.db import models
from datetime import datetime ,timedelta
from django.contrib.auth.models import User


class Client(models.Model):
    first_name=models.CharField(max_length=100 , null=False , blank=False)
    last_name=models.CharField(max_length=100 , null=False , blank=False)
    email=models.EmailField(null=True , blank=True)
    fb_account=models.URLField(null=True , blank=True)

class Plan(models.Model):
    speeds = {
        (4,4),
        (8,8),
        (16,16),
        (32,32),
    }
    periods = {
        ('1 month',1),
        ('3 months',3),
        ('6 months',6),
        ('12 months',12),
    }
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500,null=True,blank=True,help_text="enter details")
    speed = models.PositiveSmallIntegerField(choices=speeds)
    duration = models.DurationField(choices=periods)
    cost = models.PositiveSmallIntegerField()

class Subscription(models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    plan = models.OneToOneField(Plan, on_delete=models.DO_NOTHING)
    subscription_date = models.DateField()

    def sub_end_date(self):
        return self.subscription_date + timedelta(months= self.plan.duration)
    
    def remaining_period(self):
        pass

