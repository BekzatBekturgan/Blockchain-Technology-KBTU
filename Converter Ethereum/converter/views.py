import requests

from django.shortcuts import render, redirect
from django.http import HttpResponse

    
def base(request):
    content = {
        'amount': 0,
    }
    if request.method == 'GET':
        return render(request, 'base.html', content)
    else:
        try:
            amount = float(request.POST['amount'])
        except Exception:
            amount = 0
        content['amount'] = amount
        if request.POST['country'] == 'Ethereum':
            content['res'] = 355.23 * amount
        else:
            content['res'] = 53.76 * amount
        return render(request, 'base.html', content)
