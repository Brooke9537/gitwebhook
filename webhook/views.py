# django import
# from django.http import HttpResponse
from django.http.response import JsonResponse

# code import
import os
import subprocess
import json

def index(request):
    if(request.method == 'POST'):
        postbody = request.body
        result = json.loads(postbody.decode())
        refs_name = result['repository']['name']

        
        script_file = os.popen('sh script/hook.sh %s'%refs_name) 
        results = script_file.read()
        script_file.close()


        json_res = {'status':1,'result':results}

        return JsonResponse(json_res)
    else:
        
        status = 1
        output = "Method Not Allowed!"
        json_res = {'status':status,'result':output}

        return JsonResponse(json_res)
        