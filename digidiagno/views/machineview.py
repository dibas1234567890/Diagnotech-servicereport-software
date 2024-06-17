from django.http import JsonResponse
from django.views import View 
from django.shortcuts import redirect, render, get_object_or_404, HttpResponse
from digidiagno.models.machinemodel import MachineModel
from digidiagno.forms.machine_add_form import MachineAddForm
from django.contrib.auth.decorators import *
from django.core.paginator import Paginator


@login_required 
class MachineView(View):
    @login_required
    def view_machine(request):
       machine =  MachineModel.objects.all()
       paginator = Paginator(machine,25)
       page_number = request.GET.get('page')
       page_obj = paginator.get_page(page_number)
       return render(request, 'view_machine.html', {'machine':page_obj, 'page_obj':page_obj}) 
    
    @login_required
    def view_machine_by_id(request, machine_id):
       list_machines =  MachineModel.objects.filter(pk = int(machine_id))
       paginator = Paginator(list_machines,2)
       page_number = request.GET.get('page')
       page_obj = paginator.get_page(page_number)
       return render(request, 'view_machine.html', {'machine':page_obj, 'page_obj':page_obj}) 
    
    @login_required
    def add_machines(request):
      if request.method == 'POST':
        mform = MachineAddForm(request.POST)
        if mform.is_valid():
            mform.save()
            return redirect('success')
      else:
        mform = MachineAddForm()
      return render(request, 'add_machines.html', {'form': mform})
    
    def machine_add_success(request):
       return render(request, 'success_page.html')

    @login_required
    def update_machines(request,client_id):
       client = MachineModel.objects.filter(pk = int(client_id))
       form = MachineAddForm(request.POST)
       if request.method == 'POST':
          
          if form.is_valid():
             form.save()
             return redirect('view_machines.html')
          else: 
             form  = MachineAddForm(instance=client)
       return render(request, 'machines.html', {'form':form})
  
  


    def machine_get(request):
      client_id = request.GET.get('client_id')
      print(client_id, "client id is ")
      machines = MachineModel.objects.filter(client_id=client_id)
      options = [{'id':machine.id, 'name': machine.machine_name} for machine in machines]
      return JsonResponse({'options': options})



   
     
      
    
   