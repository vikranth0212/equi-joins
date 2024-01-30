from django.shortcuts import render
from app.models import *
# Create your views here.

def equijoin(request):
    EMO=Emp.objects.select_related('deptno').all()
    d={'EMO' : EMO}
    return render (request,'equijoin.html',d)

    #select_related for 1 to 1,t 10 many
    #prefetch_related for 1 to 1,1 to many,many to 1,many to many