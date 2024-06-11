"""
URL configuration for digidiagno project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views import View
from digidiagno.views import pdfExport
from digidiagno.views.table_export import table_exporter
from digidiagno.views.clientview import ClientView
from digidiagno.views.index import Index
from digidiagno.views.login import Login
from digidiagno.views.machineview import MachineView
from digidiagno.views.problemview import ProblemView

from digidiagno.views.engineering_form_view import EngineeringFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('clients/', ClientView.view_clients, name='view_clients'),
    path('machines/', MachineView.view_machine, name='view_machine'),

    path('success_page/', ClientView.client_add_success, name='success'),

    path('add-clients/', ClientView.add_clients, name='add_client'),
    path('update-clients/<int:client_id>/', ClientView.update_clients),
    path('clients/<int:client_id>/', ClientView.view_clients_by_id, name = "client_by_id"),
    path('clients/<str:client_name>/', ClientView.view_clients_by_name, name = "client_by_name"),

    path('add-machines/', MachineView.add_machines, name = "add_machine"),
    path('update-machines/<int:client_id>/', MachineView.update_machines, name = "update_machine"),
    path('machines/<int:machine_id>/', MachineView.view_machine_by_id, name = "machine_by_id"),

    path('register/', Index.register, name = 'register'),
    path('login/', Login.user_login, name = 'login'),
    path('', Index.homepage , name='home'),

    path('problem-added/', ProblemView.add_problem , name='problem'),
    path('view-problem/', ProblemView.view_all_problems , name='view_all_problems'),
    path('search-problem/', ProblemView.view_problems_by_id, name='view_problems_id'),
    path('search-problem/<str:client_name>', ProblemView.view_problems_by_name, name='view_problems_name'),
    path('search-problem-by-client-name/', ProblemView.view_problems_by_name_url, name='search_problems_name'),

    path('edit-report/<int:id>', ProblemView.edit_report, name='edit_report'),
    path('client_export', table_exporter.table_export_clients_all, name='test_url'),
    path('machine_export', table_exporter.export_all_machines, name='export_all_machines'),
    path('problem_export', table_exporter.export_all_problems, name='export_all_problem'),
    path('problem_by_machine_model/<str:machine_model>', ProblemView.problem_by_machine_model, name='problem_by_machine_model'),
    path('pdfexport/<int:id>', pdfExport.exporter, name='pdfexport'),
    path('register_engineer/', Index.EngineerRegisterView, name = 'register_engineer'),


    
    

]
