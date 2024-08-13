from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from AI.AI import AI
import requests
import json
#python manage.py runserver 127.0.0.2:8000
# Create your views here.
def index(request):

    return render(request ,"pages/index.html")


def useAI(request):
    return print(request)


@api_view(["GET"])
def useAI(request):
    res = AI.AICAL(1,2,3,4)
    return Response(res)

@api_view(["POST"])
def submit_request(request):
    res = AI.AICAL(request.data['1'] , request.data['2'] ,request.data['3'] ,request.data['4'])
    requests.post("http://127.0.0.1:8000/submit-result" , json={"result":res , 'reqID' :int(request.data['reqID'])} ,headers={'Content-Type': 'application/json'})
    return Response(data=request.data,status=status.HTTP_201_CREATED)

   