from django.shortcuts import render
from django.views import View        
from .serializer import *
from .data  import *
from django.http import JsonResponse
import json
import uuid

# Create your views here.

class AllInvoices(View):
    def get(self,request):
        serializer= InvoiceSerializer(invoicesData,many=True).data
        return JsonResponse(serializer,safe=False)
    
    def post(self,request):
        data= json.loads(request.body)
        data["invoice_id"]=len(invoicesData)+1
        print(data)
        serializer=InvoiceSerializer(data=data)
        if serializer.is_valid():
           invoicesData.append(serializer.data)
           return JsonResponse(serializer.data,safe=False)
        return JsonResponse(serializer.errors,safe=False)

class SpecificInvoices(View):
    def get(self,request):
        for val in invoicesData:
            if val["invoice_id"]==id:
                serializer=InvoiceSerializer(val).data
                return JsonResponse(serializer,safe=False)
        return JsonResponse({"message":"No invoice found"})
    
class Additems(View):
    def post(self,request):
        data=json.loads(request.body)
        serializer=ItemSerializer(data=data)
        if serializer.is_valid():

          for val in invoicesData:
            if val["invoice_id"]==id:
                val["items"].append(serializer.data)
                return JsonResponse(serializer.data,safe=False)
            return JsonResponse({"message":"no invoice found"})
          return JsonResponse(serializer.errors,safe=False)
        
class SignUpView(View):
    def post(self,request):
        data=json.loads(request.body)
        data["user_id"]=len(userData)+1
        serializer=UserSerializer(data=data)
        if serializer.is_valid():
            userData.append(serializer.data)
            return JsonResponse(serializer.data,safe=False)
        return JsonResponse(serializer.errors,safe=False)
    
class SignInView(View):
    def post(self,request):
        data=json.loads(request.body)
        for val in userData:
            if val["email"]==data["email"] and val["password"]==data["password"]:
                token=str(uuid.uuid4())
                return JsonResponse({"message":"login sccessfully","token":token,"state":True})
            
        return JsonResponse({"message":"not valid credential","state":False})
    

        



