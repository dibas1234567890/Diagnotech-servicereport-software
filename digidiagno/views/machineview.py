from django.views import View 
from django.shortcuts import redirect, render, get_object_or_404, HttpResponse
from digidiagno.models.machinemodel import MachineModel
from digidiagno.forms.machine_add_form import MachineAddForm
from django.contrib.auth.decorators import *

@login_required 
class MachineView(View):
    @login_required
    def view_machine(request):
       machine =  MachineModel.objects.all()
       return render(request, 'view_machine.html', {'machine':machine}) 
    
    @login_required
    def view_machine_by_id(request, machine_id):
       machine_by_id =  MachineModel.objects.filter(pk = int(machine_id))
       
       return render(request, 'machines.html', {'machine_by_id':machine_by_id})
    
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