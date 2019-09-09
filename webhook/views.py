# django import
from django.http import HttpResponse
from django.http.response import JsonResponse

# code import
import os
import json

def index(request):
    if(request.method == 'POST'):
        postbody = request.body
        result = json.loads(postbody.decode())
        return HttpResponse(result['repository']['name'])
    else:
        #val = os.system('sh script/gitlab_waf.sh')
        p=os.popen('sh script/gitlab_waf.sh') 
        x=p.read()
        p.close()
        json_res = {'result':x}
        return  JsonResponse(json_res)
        