from django.shortcuts import render
from django.http import JsonResponse
import requests
import pprint
from .models import Address
pp = pprint.PrettyPrinter()
# Create your views here.

def index(request):
  url = 'https://www.als.ogcio.gov.hk/lookup?q={}&n=1'
  #query = 'No. 19 Science Park'
  query = 'majestic house'
  query = '80 nathan'
  
#  if request.method == 'POST' or request.method == 'GET':
#     pass

  if request.method == 'GET':
    print('GET')
    query_string = request.GET['query']
    print('query is ::'+ query_string)

  #r = requests.get(url.format(query), headers={'Accept':'application/json', 'Accept-Language':'en'})
    r = requests.get(url.format(query_string), headers={'Accept':'application/json'}).json()
    pp.pprint(r)

  
    result = Address(jsonLine=r)
    result.save()

#return JsonResponse({'Hello':'World'})
    return JsonResponse(r)
  #return HttpResponse(json.dumps(r), content_type='application/json')