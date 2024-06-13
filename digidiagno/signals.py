

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from digidiagno.models.profile  import Profile
from digidiagno.models.engineer_profile  import EngineerProfile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    print('Signal recieved', instance.username)
    if created:
        Profile.objects.create(userprofile=instance)
        print('Profile created', instance.username)
    else:
        instance.profile.save()

@receiver(post_save, sender=User)
def create_or_update_eng_profile(sender, instance, created, **kwargs):
    print('Signal recieved', instance.username)
    if created:
        EngineerProfile.objects.create(userprofile=instance)
        print('Profile created', instance.username)
    else:
        instance.EngineerProfile.save()
