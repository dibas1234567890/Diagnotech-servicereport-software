from django.views import View 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 

from django.contrib.auth.forms import AuthenticationForm 

class Login(View):
    def user_login(request):
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('home')
        else: 
            form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})