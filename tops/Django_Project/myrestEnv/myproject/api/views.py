from django.shortcuts import render
from .models import *
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.

def student(request):
    sall=Student.objects.all()
    serializer=StudentSerializer(sall,many=True)
    # serializer data convert into json format
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type="application/json")


def student_get(request):
    sall=Student.objects.get(id=2)
    serializer=StudentSerializer(sall)
    # serializer data convert into json format
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type="application/json")
