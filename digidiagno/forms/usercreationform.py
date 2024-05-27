from digidiagno.models.profile import Profile
from digidiagno.models.clientmodel import ClientModel
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email =  forms.EmailField(required=True)
    client = forms.ModelChoiceField(queryset=ClientModel.objects.all(), required=True )
    
    class Meta: 
        model = User 
        fields = ['username','email','password1','password2', 'client']
        
    def save(self, commit=True):
                user = super().save(commit=False)
                if commit:
                    user.save()
                    profile = Profile.objects.create(userprofile=user, client=self.cleaned_data['client'])
                    print(f'Profile created: {profile}')
                return user
        