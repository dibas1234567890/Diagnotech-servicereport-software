from typing import __all__
from django import forms
from digidiagno.models.machinemodel import MachineModel
 

class MachineAddForm(forms.ModelForm):
    class Meta:
        model = MachineModel
        fields = '__all__'
    
