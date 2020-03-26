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
        result = json.loads(postbody.decode('utf-8'))
        print(postbody)
        print(result)
        
        # old way
        # script_file = os.popen('sh script/hook.sh %s'%refs_name) 
        # results = script_file.read()
        # script_file.close()

        # new way
        #status ,output = subprocess.getstatusoutput('../script/hook.sh %s' %refs_name)
        
        #json_res = {'status':status,'result':output}

        return JsonResponse(result)
    else:
        status = 0
        output = "Method Not Allowed!"
        json_res = {'status':status,'result':output}

        return JsonResponse(json_res)
        