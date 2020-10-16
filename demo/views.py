from django.shortcuts import render
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Details
from .import models
from .import serializers
from rest_framework import viewsets
from .serializers import detailSerializer
from django.http import HttpResponse,HttpResponseRedirect
from rest_framework.decorators import api_view


class get_details(viewsets.ModelViewSet):
    queryset = models.Details.objects.all() 
    serializer_class =serializers.detailSerializer

     #return Response(serialize_details.data)

def home(request):
    return render(request,'index.html')        

@api_view(['PUT', ])
def profileupdate(request,pk):
    p = Details.objects.get(id=pk)
    if request.method == "PUT":
        serializer = serializers.detailSerializer(p,data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['sucess'] = 'update sucessful'
            return Response(data=data)        
        return Response(serializer.errors)
    return(HttpResponse("hello"))     
