from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import project
from faker import Faker

# Create your views here.

def index(request):
    return render(request,'index.html')
def randomFunction(request):
    #delete all objects in project
    objects = project.objects.all().delete()
    #Generating radom number
    faker=Faker()
    for _ in range(1,30):
        project.objects.create(id=faker.pyint(),name=faker.name(),address=faker.address())
    #Displaying random numbers
    res = ''
    obj = project.objects.order_by('id')
    for elt in obj: 
        res += str(elt.id) + ' | ' + elt.name + ' | ' + elt.address +'<br>'
    return HttpResponse(res)
