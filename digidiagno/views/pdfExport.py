import datetime
from django.http import FileResponse
from django.shortcuts import render
from django.views import View 
from fillpdf import fillpdfs 
from digidiagno.models.clientmodel import ClientModel
from digidiagno.models.engineer_profile import EngineerProfile
from digidiagno.models.problemmodel import ProblemModel
from django.shortcuts import redirect, render, get_object_or_404, HttpResponse

class pdfExport(View):
   
    

    def exporter(request, id):
    
        path = 'digidiagno/static/pdf/template (8).pdf'
        form_fields = list(fillpdfs.get_form_fields(path))
        client_export = ProblemModel.objects.get(pk=id)
        print(client_export.engineer.id)
        
        try:
            global engineer_for_pdf 
            engineer_for_pdf = EngineerProfile.objects.get(userprofile_id = client_export.engineer.id)
            print(engineer_for_pdf.phone_number)
        except Exception as e: 
            print(e)


        filename_dynamic =str(client_export.date.date()) + '-' + str(client_export.name) + str(datetime.datetime.now().time()).replace(':','-') + '.pdf'
        print((form_fields))
        data_dict = {
                form_fields[0] : client_export.engineer.username,
                form_fields[1] : client_export.date.date(),
                form_fields[2] : client_export.client.client_name,
                form_fields[3] : client_export.client.client_address,
                form_fields[4] : client_export.client.warranty_amc_status,
                form_fields[5] : client_export.machine.install_location,
                form_fields[6] : client_export.name,
                form_fields[7] : client_export.system_down,
                form_fields[8] : client_export.backup,
                form_fields[9] : client_export.machine.model,
                form_fields[10] : client_export.machine.model,
                form_fields[11] : client_export.machine.model,
                form_fields[12] : client_export.machine.machine_serial_number,
                form_fields[13] : client_export.client.client_name,
                form_fields[14] : client_export.date.date(), #service rendered --- detailed_desc
                form_fields[15] : client_export.date.time(), # problem_area  = defects 
                form_fields[16] : client_export.service_rendered, # remarks is engineeros remarks 
                form_fields[17] : client_export.defects,  
                form_fields[18] : client_export.status_after_service ,
                form_fields[19] : client_export.remarks,
                form_fields[20] : client_export.date.date(),
                form_fields[21] : client_export.end_date,
                form_fields[22] : client_export.client.client_name,
                form_fields[23] : client_export.client.client_name,
                form_fields[24] : client_export.client.contact_number,
                form_fields[25] : client_export.client.contact_email,
                form_fields[25] : client_export.client.signature,
                form_fields[26] : client_export.end_date,
                form_fields[27] : client_export.client.signature,

                


                
                

                
            }
        export_pdf = fillpdfs.write_fillable_pdf(path, filename_dynamic, data_dict, flatten=True)
        
        response = FileResponse(open(filename_dynamic, "rb"), as_attachment=True,)
        return response


   