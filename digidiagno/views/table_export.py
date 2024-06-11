import csv
import pandas  as pd
from django.views import View 
from django.shortcuts import redirect, render, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import *
from digidiagno.models import *
from digidiagno.models.problemmodel import ProblemModel

@login_required
class table_exporter(View):
    def table_export_clients_all(request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename = client.csv'

        writer = csv.writer(response)
        clients = ClientModel.objects.all()
        machines = MachineModel.objects.exclude(client=None)

        writer.writerow([ 'client_id', 'client_name','client_address', 'client_contact','machine_sno'])
        for machine in machines:
            client = machine.client
            writer.writerow([client.id, client.client_name, client.client_address, client.client_contact, machine.machine_serial_number])
        client_without_machines = clients.exclude(id__in=machines.values('client_id'))
        for client in client_without_machines:
            writer.writerow([client.id, client.client_name, client.client_address, client.client_contact, 'No machine assigned yet'])
        return response
    
    def export_all_machines(request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename = machines.csv'
        writer = csv.writer(response)
        machines = MachineModel.objects.all()
        writer.writerow([ 'Machine ID', 'Client','Name', 'Machine Serial Number'])

        for machine in machines:
            writer.writerow([machine.id, machine.client, machine.machine_name, 
                           machine.machine_serial_number])
        return response
    def export_all_problems(request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename = problems.csv'
        writer = csv.writer(response)
        problem_set = ProblemModel.objects.all()
        writer.writerow([ 'Problem ID', 'Client','Machine', 'Engineer', 'Date', 'Service Rendered', 'Detailed Desc', 'Name', 'Status', 'Image'])

        for problem in problem_set:
            writer.writerow([problem.id, problem.client, problem.machine, 
                        problem.engineer, problem.date, problem.remarks, 
                        problem.service_rendered, problem.name,problem.status,
                        problem.image])
        return response



    
