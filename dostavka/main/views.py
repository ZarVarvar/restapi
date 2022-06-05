from django.shortcuts import render
from .models import Order
import json, requests
# Create your views here.

def index(request):
    response = requests.get("http://127.0.0.1:8000/api/orders")
    json_format = response.text
    obj = json.loads(json_format)

    namefirm = 'ООО "Школьная ручка"'
    addressfirm = 'г. Чита ул. Бабушкина д.128'

    record = Order.objects.all()
    record.delete()

    for i in range(len(obj)):
        nametovar = obj[i]['tovarname']
        fio = obj[i]['name']
        email = obj[i]['email']
        phone = obj[i]['phone']
        address = obj[i]['address']

        o = Order()
        o.sender = namefirm
        o.senders_address = addressfirm
        o.shipped_item = nametovar
        o.FIO = fio
        o.email = email
        o.phone_number = phone
        o.address_recipient = address
        o.save()

    if 'query' in request.GET:
        q = request.GET['query']
        order = Order.objects.filter(email=q)
    else:
        return render(request, 'main/index.html')
    return render(request, 'main/index.html', {'order': order})



