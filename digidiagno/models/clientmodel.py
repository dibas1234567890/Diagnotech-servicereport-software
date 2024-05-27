from django.db import models

class ClientModel(models.Model):
    client_name = models.CharField( max_length=50)
    client_address = models.CharField( max_length=50)
    client_contact = models.CharField( max_length=50)
    
    def __str__(self):
                return self.client_name
    
    def get_default_client(self):
            id = ClientModel.objects.first().id
            return id