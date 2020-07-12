from django.shortcuts import render
from .models import Destination
from django.http import HttpResponse
import pdb
# Create your views here.
def index(request) :
    return HttpResponse("Hello")
def home(request):
    return render(request,'home.html')
def dynhome(request):
    return render(request,'dynhome.html',{'name':'niki'})
def addnum(request):
    return render(request,'addnum.html')
def add(request):
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    res = val1 + val2
    return render(request,'result.html', {'result':res})
def travello(request):
    dests = Destination.objects.all()
    
    return render(request,'index.html', {'dests':dests})
    