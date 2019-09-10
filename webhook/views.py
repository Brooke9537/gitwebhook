# django import
# from django.http import HttpResponse
from django.http.response import JsonResponse

# code import
import os
import json

def index(request):
    if(request.method == 'POST'):
        postbody = request.body
        result = json.loads(postbody.decode())
        refs_name = result['repository']['name']

        script_file = os.popen('sh script/'+refs_name+'.sh') 
        results = script_file.read()
        script_file.close()
        json_res = {'result':results}

        return JsonResponse(json_res)
    else:
        os.system('cd /opt/md && git pull ')
        status ,output = commands.getstatusoutput('cd /opt/md && git pull ')
        #json_res = {'result':"Method not allowed!"}
        json_res = {'status':status,'result':output}

        return JsonResponse(json_res)
        