from typing import __all__
from django import forms
from django.db import models
from django.contrib.auth.models import User
from digidiagno.models.clientmodel import ClientModel
from digidiagno.models.engineer_profile import EngineerProfile
from digidiagno.models.machinemodel import MachineModel
from digidiagno.models.problemmodel import ProblemModel
from digidiagno.models.profile import Profile as profile
from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget

class ProblemForm(forms.ModelForm):
    client_signature = JSignatureField(widget=JSignatureWidget(jsignature_attrs={'color': 'black', 'border':'solid', 'ResetButton':'green'}))

    end_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), required=False)
    class Meta:
        model = ProblemModel
        fields = ['client',  'machine', 'engineer', 'end_date','remarks', 'status_after_service', 
                  'location_of_problem', 'service_rendered', 
                  'name', 'status', 'image', 'defects', 'system_down', 'client_signature']

        
    def __init__(self,  *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProblemForm,self).__init__(*args, **kwargs)
        print('init called')
        print(f'{user}')
        print('Is Client:',hasattr(user, 'profile'))
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
            
        if user and hasattr(user, 'engineerprofile') :
            print('inside if statement of engineer')
            print(User.objects.filter(username=user.engineerprofile.userprofile))
            self.fields['engineer'].queryset = User.objects.filter(username=user.engineerprofile.userprofile)
            self.fields['engineer'].initial = user.engineerprofile.userprofile
            self.fields['engineer'].widget.attrs['readonly'] = True
            self.fields['engineer'].widget.attrs['disabled'] = 'disabled'
            def clean_client(self):
                return self.initial['client']
      
