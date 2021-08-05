from django.http import HttpResponse
from django.shortcuts import render
from mysite import settings

# Create your views here.

def home(request):
    return render(request,'submit.html')

def verify(request):
    statics=[settings.STATIC_ROOT,settings.STATICFILES_DIRS]
    return render(request,'result.html',{"result":request.POST,"statics":statics})