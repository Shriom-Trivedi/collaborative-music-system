from django.shortcuts import render
from django.http import HttpResponse

# Create your views/endpoints here.
def main(request):
    return HttpResponse("Hello world")