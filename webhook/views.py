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
        for alert in result['alerts']:
            if alert["status"]=='resolved':
                message = '''Status: %s \nDetail: <a href="%s">%s</a> \n%s \nRecovery Date: %s'''%(alert["status"],alert["generatorURL"],alert["annotations"]["description"],alert["startsAt"],alert["endsAt"])
            else:
                message = '''Status: %s \nDetail: <a href="%s">%s</a> \n%s'''%(alert["status"],alert["generatorURL"],alert["annotations"]["description"])
        print(message)
        status ,output = subprocess.getstatusoutput('/opt/gitwebhook/script/alert.sh %s',message)
        # old way
        # script_file = os.popen('sh script/hook.sh %s'%refs_name) 
        # results = script_file.read()
        # script_file.close()

        # new way
        #status ,output = subprocess.getstatusoutput('../script/hook.sh %s' %refs_name)
        
        json_res = {'status':status,'result':output}
        #print(json_res)
        return JsonResponse(result)
    else:
        status = 0
        output = "Method Not Allowed!"
        json_res = {'status':status,'result':output}

        return JsonResponse(json_res)
        