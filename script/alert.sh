#!/bin/bash
# $1: 发送内容

curl 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=a790cd8d-547e-4506-888d-e3401b57e695' \
    -H 'Content-Type: application/json' \
    -d '
    {
        "msgtype": "text",
        "text": {
        "content": "'$1'"         
        }
    }'
