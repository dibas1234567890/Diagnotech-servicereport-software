from django import forms
from django.contrib.auth.models import User
from digidiagno.models.clientmodel import ClientModel
from digidiagno.models.engineer_profile import EngineerProfile
from digidiagno.models.machinemodel import MachineModel
from digidiagno.models.problemmodel import ProblemModel
from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget

class ProblemForm(forms.ModelForm):
    client_signature = JSignatureField(widget=JSignatureWidget(jsignature_attrs={'color': 'black', 'border': 'solid', 'ResetButton': 'green'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), required=False)
    
    class Meta:
        model = ProblemModel
        fields = ['client', 'machine', 'engineer', 'end_date', 'remarks', 'status_after_service', 
                  'location_of_problem', 'service_rendered', 'name', 'status', 'image', 'defects', 
                  'system_down', 'client_signature']
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProblemForm, self).__init__(*args, **kwargs)

        if user and hasattr(user, 'profile'):
            client = user.profile.client
            self.fields['client'].queryset = ClientModel.objects.filter(id=client.id)
            self.fields['client'].initial = client
            self.fields['client'].widget.attrs['readonly'] = True
            self.fields['client'].widget.attrs['disabled'] = 'disabled'
            self.fields['machine'].queryset = MachineModel.objects.filter(client=client)


        if user and hasattr(user, 'engineerprofile'):
            engineer = user.engineerprofile.userprofile
            self.fields['engineer'].queryset = User.objects.filter(username=engineer)
            self.fields['engineer'].initial = engineer
            self.fields['engineer'].widget.attrs['readonly'] = True
            self.fields['engineer'].widget.attrs['disabled'] = 'disabled'

    def clean_client(self):
        return self.cleaned_data.get('client', self.initial.get('client'))
