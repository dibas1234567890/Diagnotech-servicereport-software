from typing import Any, Mapping, __all__
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from digidiagno.models.clientmodel import ClientModel
from django.contrib.auth import authenticate
from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget

class ClientAddForm(forms.ModelForm):


    class Meta:
        model = ClientModel
        fields = '__all__'
    