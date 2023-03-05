from django.db import models
from datetime import datetime ,timedelta
# Create your models here.
class client(models.Model):
    First_name=models.CharField(max_length=100 , null=False , blank=False)
    last_name=models.CharField(max_length=100 , null=False , blank=False)
    email=models.EmailField(null=True , blank=True)
    fb_account=models.URLField(null=True , blank=True)
def finished():
    return datetime.today() + timedelta(days=30)

class subscription_account(models.Model):
    client = models.ForeignKey(client, related_name="dweets", on_delete=models.DO_NOTHING)
    date_subscription = models.DateTimeField(auto_now_sub=True)
    subscription_period=  models.DateField (default= finished)
