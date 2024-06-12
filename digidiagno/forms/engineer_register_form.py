from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from digidiagno.models.engineer_profile import EngineerProfile
from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget


class EngineerRegisterForm(UserCreationForm):
    phone = forms.CharField(max_length=100, required=False)
    designation = forms.CharField(max_length=100, required=False)
    is_this_user_engineer = forms.BooleanField(required=False)
    signature = JSignatureField(widget=JSignatureWidget(jsignature_attrs={'color': '#489755', 'border':'solid', 'ResetButton':'green'}))

    class Meta: 
        model = User
        fields = ('username', 'email', 'phone', 'password1', 'password2', 'designation', 'signature')
        

    def save(self, commit=True):
            user = super().save(commit=True)
            if commit:
                user.save()
                profile = EngineerProfile.objects.create(userprofile=user, designation=self.cleaned_data['designation'], 
                                                            phone_number = self.cleaned_data['phone'], 
                                                            signature = self.cleaned_data['signature'], 
                                                            is_engineer = self.cleaned_data['is_this_user_engineer'])
                print(f'Profile created: {profile}')
            return user
        