import base64
import datetime
from io import BytesIO
import os
from tkinter import Image
from django.http import FileResponse
from django.shortcuts import render
from django.views import View 
from fillpdf import fillpdfs
from digidiagno.models.clientmodel import ClientModel
from digidiagno.models.engineer_profile import EngineerProfile
from digidiagno.models.problemmodel import ProblemModel
from django.shortcuts import redirect, render, get_object_or_404, HttpResponse
from jsignature.utils import draw_signature
from PIL import Image



class pdfExport(View):
    filename_dynamic = None
      
 
    def exporter(request, id):
        print(id)
    
        path = 'digidiagno/static/pdf/template (9).pdf'
        path_sign = 'digidiagno/static/pdf/template (10) sign.pdf'
        path_sign_final = 'digidiagno/static/pdf/template (11) sign.pdf'

        
        form_fields = list(fillpdfs.get_form_fields(path))
        client_export = ProblemModel.objects.get(pk=id)
        print("id is", client_export.engineer.id)

        signature_for_pdf = client_export.client_signature
        test = EngineerProfile.objects.get(userprofile_id = 2)
        print(test.id)
        try:
            global engineer_for_pdf 
            engineer_for_pdf = EngineerProfile.objects.get(userprofile_id = client_export.engineer.id)
            print(engineer_for_pdf.phone_number)
        except Exception as e: 
            print(e)

        signature_client = draw_signature(client_export.client_signature, as_file=True)
        engineer_signature = draw_signature(engineer_for_pdf.signature, as_file=True)
      
        fillpdfs.place_image(signature_client, 75, 655, path, path_sign, 1, width=50, height=50 )
        fillpdfs.place_image(engineer_signature, 300, 75, path_sign, path_sign_final, 1, width=50, height=50 )

        # signature_image = Image.open(BytesIO(signature_image_data))
        # signature_image_path = 'temp_signature.png'
        # signature_image.save(signature_image_path)

        global filename_dynamic
        #filename_dynamic = str(client_export.date.date()) + '-' + str(client_export.name) + str(datetime.datetime.now().time()).replace(':','-') + '.pdf'
        filename_dynamic = 'new.pdf'
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
                form_fields[26] : signature_client,
                form_fields[27] : client_export.end_date,
                form_fields[28] : engineer_for_pdf.signature,

                


                
                

                
            }
        
        export_pdf = fillpdfs.write_fillable_pdf(path_sign_final, filename_dynamic, data_dict, flatten=True)
        
        response = FileResponse(open(filename_dynamic, "rb"), as_attachment=True)
        
        
        return response
    
    
    

    # def file_cleaner(filename_dynamic):
    #     try: 
    #         if filename_dynamic: 
    #             os.remove(filename_dynamic)
    #     except Exception as e:
    #         print(e)

    # file_cleaner( filename_dynamic = filename_dynamic)




   