# django import
# from django.http import HttpResponse
from django.http.response import JsonResponse

# code import
import os
import subprocess
import json
import requests
import time, datetime

def trans_time(time_trans):
    time_strip = time.strptime(time_trans[:19], "%Y-%m-%dT%H:%M:%S")
    time_transed = time.strftime("%Y-%m-%d %H:%M:%S", time_strip)
    return time_transed

def index(request):
    if(request.method == 'POST'):
        postbody = request.body
        result = json.loads(postbody.decode('utf-8'))
        for alert in result['alerts']:
            if alert["status"]=='resolved':
                message = "> Status: OK \nDetail: [%s](%s) \n%s \nRecovery Date: %s"%(alert["annotations"]["description"],alert["generatorURL"],trans_time(alert["startsAt"]),trans_time(alert["endsAt"]))
            else:
                message = "> Status: PROBLEM \nDetail: [%s](%s) \n%s"%(alert["annotations"]["description"],alert["generatorURL"],trans_time(alert["startsAt"]))

            url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=a790cd8d-547e-4506-888d-e3401b57e695"
            payload = "{\"msgtype\": \"markdown\",\"markdown\": {\"content\": \"%s\"}}"%message
            headers = {
            'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data = payload)
            json_res = {'status':response.status_code,'result':response.text}
            
        return JsonResponse(json_res)
    else:
        status = 0
        output = "Method Not Allowed!"
        json_res = {'status':status,'result':output}

        return JsonResponse(json_res)
        
