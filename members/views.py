from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context  = {
        'mymembers': mymembers
    }
    return HttpResponse(template.render(context,request))

def details(request,id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context  = {
        'mymember': mymember
    }
    return HttpResponse(template.render(context,request))

def testing(request):
    template = loader.get_template('testing.html')
    testingobject = ["apple", "banana", "cherry"]
    is_list = isinstance(testingobject, list)
    context  = {
        'testingobject': testingobject,
        'is_list': is_list
    }
    return HttpResponse(template.render(context,request))
