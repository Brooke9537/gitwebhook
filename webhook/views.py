# django import
from django.http import HttpResponse

# code import
import os

def index(request):
    #val = os.system('sh script/gitlab_waf.sh')
    p=os.popen('sh script/gitlab_waf.sh') 
    x=p.read()
    p.close()
    return HttpResponse(x)
    
