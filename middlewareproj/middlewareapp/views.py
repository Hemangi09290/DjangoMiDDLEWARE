from asyncio.log import logger
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

def hello(request):
   return HttpResponse("Hello, Django!")


# Create your views here.
def home(request):
	print("This is a View call")
	return render(request,'home.html')

def some_view(request):
	logger.warning('This is a Logger example')
	return HttpResponse("Hello, Logger Example")