from django.shortcuts import render

# Create your views here.
import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


from django.views.decorators.csrf import csrf_exempt

# http://localhost:8005/cambio_moneda?base=USD&target=EUR&amount=100
@api_view(['GET'])
def cambio_moneda(request):
    # Coger datos del request
    base = request.GET.get('base')
    target = request.GET.get('target')
    amount = request.GET.get('amount')
    
    # API key
    api_key = 'fca_live_QPBC0YFuIWrZnyqdqgX5K5uPUAbvWPrHP9vASabh'
    
    # API URL
    api_url = f"https://api.freecurrencyapi.com/v1/latest?apikey={api_key}&base_currency={base}&currencies={target}"
    
    # Realiza una solicitud GET a la API
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        result = float(amount) * float(data['data'][target])
        return Response({"resultado" : result})
    else:
        return Response({"error": "Error al convertir moneda"}, status=500)