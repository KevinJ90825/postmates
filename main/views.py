from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from postmates.helpers import GeocodeHelper


def index(request):
    return render(request, 'index.html')

def geocode(request):
    if not request.GET['address'] or len(request.GET['address']) == 0:
        return HttpResponse(status=400, content="Must include address parameter")
    response = GeocodeHelper.query_address(
        request.GET['address'], service=request.GET.get('service', 'google'))
    return JsonResponse(response)
