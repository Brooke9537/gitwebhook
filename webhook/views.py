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
        refs_name = result['repository']['name']

        p=os.popen('sh script/'+refs_name+'.sh') 
        x=p.read()
        p.close()
        json_res = {'result':x}

        return JsonResponse(json_res)
    else:
        return HttpResponse("Method not allowed!")
        