# django import
from django.http import HttpResponse
from django.http.response import JsonResponse
import json

# code import
import os

def index(request):
    if(request.method == 'POST'):
        postbody = request.body
        json_data = json.loads(postbody)
        return HttpResponse(json_data['payload']['repository']['name'])
    else:
        #val = os.system('sh script/gitlab_waf.sh')
        p=os.popen('sh script/gitlab_waf.sh') 
        x=p.read()
        p.close()
        json = {'result':x}
        return  JsonResponse(json)
        