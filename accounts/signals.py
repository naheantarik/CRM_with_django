from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Customer


def CustomerProfile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)

        Customer.objects.create(
            user=instance,
            name=instance.username,
            email=instance.email
        )


post_save.connect(CustomerProfile, sender=User)
