from django.db import models
from django.contrib.auth.models import User
from digidiagno.models.clientmodel import ClientModel
from digidiagno.models.machinemodel import MachineModel

status_choices= (('Resolved','Resolved'),
                  ('Ongoing','Ongoing'), 
                  ('Processing','Processing'), 
                  ('NA','NA'))

class ProblemModel(models.Model):
        client = models.ForeignKey(ClientModel, null=True, blank=True, related_name='problem_client', on_delete=models.CASCADE)
        machine = models.ForeignKey(MachineModel, null=True,blank=True, related_name='problem_machine', on_delete=models.CASCADE)
        
        engineer = models.ForeignKey(User, on_delete=models.CASCADE)
        date = models.DateField(auto_now=True)
        remarks = models.CharField(max_length=1024)
        detailed_desc = models.CharField(max_length=2048)
        name = models.CharField(max_length=50)
        status = models.CharField(max_length=100, choices=status_choices, default='Processing')
        image = models.ImageField(upload_to='static/media/img/report_uploads', height_field=None, null=True, blank=True, width_field=None, max_length=None)
        
        class Meta:
            ordering = ['-id']
        
        def __str__(self):
                return self.name
