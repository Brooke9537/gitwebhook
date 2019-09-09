# django import
from django.http import HttpResponse
from django.http.response import JsonResponse

# code import
import os

def index(request):
    #val = os.system('sh script/gitlab_waf.sh')
    p=os.popen('sh script/gitlab_waf.sh') 
    x=p.read()
    p.close()
    json = {'result':x}
    return  JsonResponse(json)
    
