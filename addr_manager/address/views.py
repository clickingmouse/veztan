from django.shortcuts import render
from django.http import JsonResponse
import requests
import pprint
pp = pprint.PrettyPrinter()
# Create your views here.

def index(request):
  url = 'https://www.als.ogcio.gov.hk/lookup?q={}&n=1'
  #query = 'No. 19 Science Park'
  query = 'majestic house'
  query = '80 nathan'

  r = requests.get(url.format(query), headers={'Accept':'application/json', 'Accept-Language':'en'})
  r = requests.get(url.format(query), headers={'Accept':'application/json'}).json()


  pp.pprint(r)


  return JsonResponse({'Hello':'World'})