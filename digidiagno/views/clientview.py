from django.views import View 
from django.shortcuts import redirect, render, get_object_or_404, HttpResponse
from digidiagno.decorators import group_required
from digidiagno.models.clientmodel import ClientModel
from digidiagno.forms.client_add_form import ClientAddForm
from django.contrib.auth.decorators import *



from digidiagno.models.machinemodel import MachineModel

@login_required
@group_required('admin')
class ClientView(View):
    @login_required
    def view_clients(request):
       clients =  ClientModel.objects.all()
       return render(request, 'view_clients.html', {'clients':clients}) 
    
    @login_required
    def view_clients_by_id(request, client_id):
       clients_by_id =  ClientModel.objects.filter(pk = int(client_id))
       
       return render(request, 'clients.html', {'clients_by_id':clients_by_id})
    @login_required
    def view_clients_by_name(request, client_name):
       clients_by_name =  ClientModel.objects.filter(client_name__icontains = client_name)
       
       return render(request, 'clients.html', {'clients_by_name':clients_by_name})
    
    @login_required
    def add_clients(request):
      if request.method == 'POST':
        form = ClientAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
      else:
        form = ClientAddForm()
      return render(request, 'add_clients.html', {'form': form})
    
    def client_add_success(request):
      return render(request, 'success_page.html')

    @login_required
    def update_clients(request,client_id):
       client = ClientModel.objects.filter(pk = int(client_id))
       form = ClientAddForm(request.POST)
       if request.method == 'POST':
          
          if form.is_valid():
             form.save()
             return redirect('view_clients.html')
          else: 
             form  = ClientAddForm(instance=client)
       return render(request, 'clients.html', {'form':form})
    