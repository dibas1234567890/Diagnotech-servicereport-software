from django.db import models

from digidiagno.models.clientmodel import ClientModel
status_choices = (('cobas c 111', 'cobas c 111'),
('cobas c 311', 'cobas c 311'),
('cobas e 411', 'cobas e 411'),
('cobas link (all versions)', 'cobas link (all versions)'),
('ISE 9180', 'ISE 9180'),
('COBAS INTEGRA 400 plus', 'COBAS INTEGRA 400 plus'),
('BenchMark GX', 'BenchMark GX'),
('cobas 6000 core unit', 'cobas 6000 core unit'),
('cobas e 601', 'cobas e 601'),
('COBAS AMPLIPREP', 'COBAS AMPLIPREP'),
('COBAS TaqMan', 'COBAS TaqMan'),
('BenchMark XT/LT', 'BenchMark XT/LT'),
('COBAS TaqMan 48', 'COBAS TaqMan 48'),
('FortiGate-50E', 'FortiGate-50E'),
('LightCycler 480', 'LightCycler 480')
 
                )

class MachineModel(models.Model):
        machine_name = models.CharField( max_length=50, unique=True)
        machine_serial_number = models.CharField(max_length=50, unique=True)
        client = models.ForeignKey(ClientModel, null=True, blank=True, related_name='machine', on_delete=models.CASCADE)
        model = models.CharField(max_length=100, choices=status_choices, default='Processing')
        
        class Meta:
            ordering = ['-id']

        def __str__(self):
                return self.machine_serial_number

