from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from Users.models import Users
from .models import PrototypeToken
from .models import PrototypeRequestDB
from Users.serializer import serializer as Users_Serializer
from .serializer import serializer as Token_Serializer 
from .serializer import serializerRequsetDB as RequestDB_Serializer 
from .PrototyeToken import * 
import requests
import json
from celery import shared_task
from django.core.mail import send_mail
import random
# Task celery
@shared_task
def send_req_AI(request):
     reqID =random.randint(1000,9999)
     data = json.dumps({"1":request.data['A'] , "2":request.data['B'] ,"3":request.data['C'] ,"4":request.data['D'] , 'reqID':int(reqID)})
     headers = {'Content-Type': 'application/json'}
     PrototypeRequestDB.objects.create(token = request.data['token'] , req = "CAL" ,reqID = int(reqID) , status ="SendToAI")
     requests.post("http://127.0.0.2:8000/submit-request" , data=data ,headers=headers)
    
# Create your views here.
def index(request):
    
    tokens =PrototypeToken.objects.all()
    tokens.delete()
    req =PrototypeRequestDB.objects.all()
    req.delete()
    return render(request ,"pages/index.html")


@api_view(["GET"])
def getdata(request):
   
    req =PrototypeToken.objects.all()
   # req.delete()
    serializer = Token_Serializer(req , many = True)
    return Response(serializer.data)

@api_view(["GET"])
def fetchRequest(request):
   
    req =PrototypeRequestDB.objects.all()
   # req.delete()
    serializer = RequestDB_Serializer(req , many = True)
    return Response(serializer.data)

@api_view(["POST"])
def postdata(request):
    user = Users_Serializer(data = request.data)
    if user.is_valid():
        try:
          findeduser = Users.objects.get(userName = request.data['userName'] , password = request.data['password'])
          if(findeduser):     
            token = CreateToken()
            submit =True
        except :
            submit =False   
            token = False    
       
    return Response(data=json.dumps({"token":token , "submit":submit}) ,status=status.HTTP_201_CREATED)

@api_view(["GET"])
def getresult_id(request ,id):
     findedreq = PrototypeRequestDB.objects.get(reqID = id)
     return Response(data=findedreq.status,status=status.HTTP_201_CREATED)    


@api_view(["POST"])
def submit_request(request):
    print(request.data)
    token = Token_Serializer(data = request.data)
    if token.is_valid():
        try:
          findtoken = PrototypeToken.objects.get(token = request.data['token'])
          if(findtoken):     
            submit =True
        except :
            submit =False   
        try:
               
                send_req_AI(request=request)
                serverproblem =False
        except:
                serverproblem =True         
    return Response(data=json.dumps({"submit":submit , "serverproblem": serverproblem}) ,status=status.HTTP_201_CREATED)   



@api_view(["POST"])
def submit_result(request):
    print(request.data['result'])
    print(request.data['reqID'])
    try:
      requests.post("http://localhost:3000/user_result_message" , data=json.dumps({"result":request.data['result']}) ,headers = {'Content-Type': 'application/json'})
      findedreq = PrototypeRequestDB.objects.get(reqID = int(request.data["reqID"]))
      findedreq.status = "Completed"
      findedreq.save()
    except:
        pass  
    return Response(status=status.HTTP_201_CREATED)
