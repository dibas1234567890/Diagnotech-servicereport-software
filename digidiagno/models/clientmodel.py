from django.db import models
choice = (('No', 'No'), ('Yes' , 'Yes' ))
class ClientModel(models.Model):
    client_name = models.CharField( max_length=50)
    client_address = models.CharField( max_length=50)
    client_contact = models.CharField( max_length=50)
    contact_number = models.CharField(max_length=50, blank=True, null=True)
    contact_email = models.CharField(max_length=50, blank=True, null=True)
    warranty_amc_status = models.CharField(max_length=50, choices=choice, blank=True, null=True)
    signature = models.ImageField(blank=True, null=True)

    class Meta:
            ordering = ['-id']
    
    def __str__(self):
                return self.client_name
    
    def get_default_client(self):
            id = ClientModel.objects.first().id
            return id