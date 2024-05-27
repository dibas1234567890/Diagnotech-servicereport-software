from django.shortcuts import redirect, render
from django.views import View
from digidiagno.forms.usercreationform import UserCreationForm, UserRegistrationForm

class Index(View):

    def homepage(request):        
        user = request.user
        return render(request, 'index.html', {'user':user})
    def register(request):
        if request.method == 'POST':
            form  = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                return redirect('login')
        else:
            form  = UserRegistrationForm(request.POST)
        return render(request, 'signup.html', {"form":form})
