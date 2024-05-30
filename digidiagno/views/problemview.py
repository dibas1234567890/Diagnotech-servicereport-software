from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from digidiagno.forms.problemform import ProblemForm
from digidiagno.models.problemmodel import ProblemModel
from django.contrib.auth.decorators import *
import urllib.parse
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator



@login_required 
 
class ProblemView(View):
  

   @login_required 
   def add_problem(request):
    if request.method == 'POST':
        problem_registerform = ProblemForm(request.POST, user=request.user)
        
        if problem_registerform.is_valid():
            problem_instance = problem_registerform.save(commit=False)
            msg ='Problem Reported'
            problem_instance.save()
            print(msg)
            try:
                profile = request.user.profile
                if profile.client is not None:
                    problem_instance.client = profile.client
            except ObjectDoesNotExist:
                # No profile or client found, continue without setting client
                pass
            
            return render(request, 'success_page.html', {'problem_added_success':msg})
            
    else:
        problem_registerform = ProblemForm(user=request.user)
    
    return render(request, 'report_problem.html', {'form': problem_registerform})
   

   @login_required 
   def view_all_problems(request):
      all_problems = ProblemModel.objects.all()
      paginator = Paginator(all_problems,25)
      page_number = request.GET.get('page')
      page_obj = paginator.get_page(page_number)
      return render(request,'all_problem.html', {'problems':page_obj, 'page_obj':page_obj})
   
   
   @login_required 
   def view_problems_by_id(request):
      query = request.GET.get('q')
      results = None
      if query:
         results = ProblemModel.objects.filter(id=query)
       
      return render(request,'search_problems.html', {'problems':results})
      
   @login_required 
   def view_problems_by_name(request, client_name):
       
      print("view_problems_by_name called")
      query = client_name
      query = urllib.parse.unquote(query)
      print(f"{query}")
      results_name = None
      no_results = False
      if query:
        print(" inside if view_problems_by_name called")
        results_name = ProblemModel.objects.filter(client__client_name__icontains=query)
        paginator = Paginator(results_name,10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        print(results_name.query)
      else:
         no_results = True
         page_obj = ProblemModel.objects.all()
      return render(request,'view_client_machine.html', {'problems_name':page_obj,'no_results':no_results, 'page_obj':page_obj })
   
   def view_problems_by_name_url(request):
      print("viewsearch called")
      client_name = request.GET.get('client')
      print(f"{client_name}")
      results_name = None
      no_results = False
      if client_name:
         results_name = ProblemModel.objects.filter(client__client_name__icontains=client_name)
         paginator = Paginator(results_name,10)
         page_number = request.GET.get('page')
         page_obj = paginator.get_page(page_number)
         return render(request,'search_client_by_name.html', {'problems_name':page_obj, 'page_obj':page_obj,'client_name':client_name })
      else:
         no_results = True
         results_name = ProblemModel.objects.all()
         paginator = Paginator(results_name,2)
         page_number = request.GET.get('page') 
         page_obj = paginator.get_page(page_number)
      print(results_name)
      return render(request,'search_client_by_name.html', {'problems_name':page_obj,'no_results':no_results, 'client_name':client_name })
   
   def search_problems(request):
      return render(request, 'search_problems.html')
   
   
   @login_required 
   def edit_report(request, id):
         success = None
         button_required = True
         obj = get_object_or_404(ProblemModel, pk=id)
    
         if request.method == 'POST':
            
            form = ProblemForm(request.POST, instance=obj)
            if form.is_valid():
               
                  form.save()
                  success = "Record Edited Succesfully"
                  button_required = False
                  return render(request, 'edit_report.html', {"success":success, "button_required":button_required})  
         else:
           
            form = ProblemForm(instance=obj)
         
         return render(request, 'edit_report.html', {'form': form, 'obj': obj,"button_required":button_required})
   
   def problem_by_machine_model(request, machine_model):
      print(machine_model)
      machine_model = urllib.parse.unquote(machine_model)


      if id:
         print('inside if condition')
         objects = ProblemModel.objects.filter(machine__model__icontains=machine_model)
         return render(request, 'view_problems_machine_by_model.html', {'objects':objects})
      else: 
         print("Error in Problem by machine name")
         msg = 'ERRRRRRRORRRRR'
         return render(request, 'test.html', {'objects':msg})




