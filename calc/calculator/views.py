from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Calculator
from .serializers import CalculatorSerializer
import requests
from django.http import JsonResponse


def even(request):
    url = 'http://20.244.56.144/numbers/even'
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)

@api_view(['GET'])
def get_even(request):
    data = even(request)
    print(data)
    return Response(data)

def odd(request):
    url = 'http://20.244.56.144/numbers/odd'
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)

@api_view(['GET'])
def get_odd(request):
    data = odd(request)
    print(data)
    return Response(data)

def fibo(request):
    url = 'http://20.244.56.144/numbers/fibo'
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)

@api_view(['GET'])
def get_fibo(request):
    data = fibo(request)
    print(data)
    return Response(data)

def rand(request):
    url = 'http://20.244.56.144/numbers/rand'
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)

@api_view(['GET'])
def get_rand(request):
    data = rand(request)
    print(data)
    return Response(data)




    

