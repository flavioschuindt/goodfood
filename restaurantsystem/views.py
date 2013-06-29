# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
import json

from models import Product

def get_product_updated_price(request, product_id):
    product = Product.objects.filter(id=product_id)
    if len(product) == 1:
        data = {'price':str(product[0].price)}
    else:
        data = {'price':''}

    data = json.dumps(data)
    return HttpResponse(data, mimetype='application/json')