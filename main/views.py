from django.http import JsonResponse
from django.shortcuts import render

from postmates.helpers import GeocodeHelper


def index(request):
    return render(request, 'index.html')

def geocode(request):
    response = GeocodeHelper.query_address(
        request.GET['address'], service=request.GET.get('service', 'google'))
    return JsonResponse(response)
