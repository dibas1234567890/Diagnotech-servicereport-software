from django.db import models

from digidiagno.models.clientmodel import ClientModel

class MachineModel(models.Model):
        machine_name = models.CharField( max_length=50)
        machine_serial_number = models.CharField(max_length=50, unique=True)
        client = models.ForeignKey(ClientModel, null=True, blank=True, related_name='machine', on_delete=models.CASCADE)
        
        def __str__(self):
                return self.machine_name

