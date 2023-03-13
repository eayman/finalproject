from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Agent
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=User)
def post_user_created(sender, instance, created, **kwargs):
    if created:
        Agent.objects.create(user=instance)

    subject = "welcome to our comunity"
    message = "nice to meet you!"

    #send_mail(subject, message,settings.EMAIL_HOST_USER, "tt8ispcrm@gmail.com", )





