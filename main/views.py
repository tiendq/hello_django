from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
  return HttpResponse('This is our homepage! It works!')
