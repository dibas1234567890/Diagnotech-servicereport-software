from django.db import models
from digidiagno.models.clientmodel import ClientModel 
from digidiagno.models.machinemodel import MachineModel


class Ownership(models.Model):
    client_id  = models.ForeignKey(ClientModel,on_delete=models.CASCADE )
