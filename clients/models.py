from django.db import models
from datetime import date ,timedelta
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Client(models.Model):
    provinces = [
    ('Gaza', 'Gaza'),
    ('North Gaza', 'North Gaza'),
    ('Central', 'Central'),
    ('Khan Yunis', ' Khan Yunis'),
    ('Rafah', 'Rafah'),
    ]
    first_name=models.CharField(max_length=100 , null=False , blank=False)
    last_name=models.CharField(max_length=100 , null=False , blank=False)
    NID = models.PositiveIntegerField(unique=True,verbose_name="National identification number")
    email = models.EmailField(null=True, blank=True,unique=True)
    address = models.CharField(max_length=50,choices=provinces, null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    created_at = models.DateField(auto_now=True, editable=False)
    
    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)

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
    created_at = models.DateField(auto_now=True, editable=False)

    def __str__(self):
        return str(self.name)


class Subscription(models.Model):

    def expiry(self):
        return self.start_date + timedelta(months= self.plan.duration)
    
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    plan = models.OneToOneField(Plan, on_delete=models.DO_NOTHING)
    start_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=expiry)

    
    def remaining_period(self):
        current_date = date.today()  
        if current_date > self.expiry_date:
            return (current_date - self.expiry_date).days 
        else:
            return 0

    def __str__(self):
        return str(self.id) + " " + str(self.client)
