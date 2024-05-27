from django.db import models
from digidiagno.models.clientmodel import ClientModel
from django.contrib.auth.models import User

from digidiagno.models.machinemodel import MachineModel

class Profile(models.Model):
    userprofile = models.OneToOneField(User, on_delete=models.CASCADE)
    client = models.ForeignKey(ClientModel, on_delete=models.SET_NULL, null=True, blank=True)
    machine = models.ForeignKey(MachineModel, on_delete= models.SET_NULL,null=True, blank=True )

    def __str__(self):
        return self.userprofile.username
