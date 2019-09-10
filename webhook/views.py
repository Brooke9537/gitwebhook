# django import
# from django.http import HttpResponse
from django.http.response import JsonResponse

# code import
import logging
import os
import subprocess
import json

logger = logging.getLogger(__name__)

def index(request):
    if(request.method == 'POST'):
        postbody = request.body
        result = json.loads(postbody.decode())
        refs_name = result['repository']['name']

        # old way to run script
        # script_file = os.popen('sh script/'+refs_name+'.sh') 
        # results = script_file.read()
        # script_file.close()

        status ,output = subprocess.getstatusoutput('cd /opt/'+refs_name+' && git pull ')
        logger.log(refs_name+"\n"+output)
        json_res = {'status':status,'result':output}

        return JsonResponse(json_res)
    else:
        
        status = 1
        output = "Method Not Allowed!"
        json_res = {'status':status,'result':output}

        return JsonResponse(json_res)
        