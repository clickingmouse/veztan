from django.shortcuts import render
from django.http import JsonResponse
import requests
# Create your views here.

def index(requests):
    return JsonResponse({'Hello':'World'})