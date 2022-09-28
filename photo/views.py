from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("행복한 우리 가족. 소중한 추억 만들기.")