
from pyexpat.errors import messages

from django.shortcuts import render
from digidiagno.forms.engineer_register_form import EngineerRegisterForm
from django.views import View
class EngineeringFormView(View):
   def register(request):
      if request == 'POST':
         registerform = EngineerRegisterForm()
         if registerform.is_valid():
            registerform.save()
         return render(request, 'success_page.html')
      else:
         registerform = EngineerRegisterForm()
         return render(request, 'signup.html', {'form':registerform})
   