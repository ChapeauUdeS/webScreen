from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
#ser.write(b'0')

# Create your views here.


def index(request):
    latest_question_list = "hello"
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def sendCommand(request, cmd=999):
    print(cmd)
    #ser.write(b'0')
    ser.write(bytes(cmd, encoding='utf-8'))
    return HttpResponse(status=204)


#ser.write(b'0')