from django.db import models
from datetime import datetime ,timedelta
# Create your models here.
class Client(models.Model):
    First_name=models.CharField(max_length=100 , null=False , blank=False)
    last_name=models.CharField(max_length=100 , null=False , blank=False)
    email=models.EmailField(null=True , blank=True)
    fb_account=models.URLField(null=True , blank=True)
def finished():
    return datetime.today() + timedelta(days=30)

class Subscription(models.Model):
    client = models.ForeignKey(Client, related_name="clients", on_delete=models.DO_NOTHING)
    date_subscription = models.DateTimeField(auto_now_sub=True)
    subscription_period=  models.DateField (default= finished)
