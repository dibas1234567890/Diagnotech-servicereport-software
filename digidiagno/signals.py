

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from digidiagno.models.profile  import Profile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    print('Signal recieved', instance.username)
    if created:
        Profile.objects.create(userprofile=instance)
        print('Profile created', instance.username)
    else:
        instance.profile.save()
