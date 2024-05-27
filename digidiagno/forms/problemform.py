from typing import __all__
from django import forms
from django.db import models
from django.contrib.auth.models import User
from digidiagno.models.clientmodel import ClientModel
from digidiagno.models.machinemodel import MachineModel
from digidiagno.models.problemmodel import ProblemModel
from digidiagno.models.profile import Profile as profile

class ProblemForm(forms.ModelForm):

    class Meta:
        model = ProblemModel
        fields = ['client', 'machine', 'engineer', 'remarks', 'detailed_desc', 'name', 'status', 'image']

        
    def __init__(self,  *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProblemForm,self).__init__(*args, **kwargs)
        print('init called')
        print(f'{user}')
        print(hasattr(user, 'profile'))
        #print(ClientModel.objects.filter(client_name=user.profile.client))
        if user and hasattr(user, 'profile'):
            print('inside if statement')
            self.fields['client'].queryset = ClientModel.objects.filter(client_name=user.profile.client)
            self.fields['client'].initial = user.profile.client
            self.fields['client'].widget.attrs['readonly'] = True
            self.fields['client'].widget.attrs['disabled'] = 'disabled'
            self.fields['machine'].queryset = MachineModel.objects.filter(client=user.profile.client)
            def clean_client(self):
                return self.initial['client']