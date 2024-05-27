from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from digidiagno.forms.problemform import ProblemForm
from digidiagno.models.problemmodel import ProblemModel
from django.contrib.auth.decorators import *

@login_required 
 
class ProblemView(View):
   @login_required 
   def add_problem(request):

      if request.method == 'POST':
         problem_registerform = ProblemForm(request.POST, user=request.user)

         if problem_registerform.is_valid():
            problem_instance = problem_registerform.save(commit=False)
            problem_instance.client = request.user.profile.client
            problem_registerform.save(commit=True)
         return render(request, 'success_page.html')
      else:
         problem_registerform = ProblemForm(user=request.user)
         return render(request, 'report_problem.html', {'form':problem_registerform})
   @login_required 
   def view_all_problems(request):
      all_problems = ProblemModel.objects.all()
      return render(request,'all_problem.html', {'problems':all_problems})
   
   
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
      print(f"{query}")
      results_name = None
      no_results = False
      if query:
         results_name = ProblemModel.objects.filter(client__client_name__icontains=query)
      else:
         no_results = True
         results_name = ProblemModel.objects.all()
      return render(request,'search_problems_client_table.html', {'problems_name':results_name,'no_results':no_results })
   
   def view_problems_by_name_url(request):
      print("viewsearch called")
      client_name = request.GET.get('client')
      print(f"{client_name}")
      results_name = None
      no_results = False
      if client_name:
         results_name = ProblemModel.objects.filter(client__client_name__icontains=client_name)
         return render(request,'search_client_by_name.html', {'problems_name':results_name})
      else:
         no_results = True
         results_name = ProblemModel.objects.all()
      print(results_name)
      return render(request,'search_client_by_name.html', {'problems_name':results_name,'no_results':no_results, 'client_name':client_name })
   
   def search_problems(request):
      return render(request, 'search_problems.html')
   
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

      



