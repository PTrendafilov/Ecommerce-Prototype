from math import prod
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
import json 
def index(request):

    products=Product.objects.all()
    for product in products:
       product.price=f"{product.price:.2f}"
       product.old_price=f"{product.old_price:.2f}"

    menu=Menu.objects.first()

    notices=Notice.objects.all()

    first_notice=Notice.objects.first()

    list_notices_count=[]

    notices_count=len(notices)    
    for i in range(1, notices_count):
       list_notices_count.append(i)

    site=Site.objects.first()

    return render(request, 'index.html', {'products':products, 'menu':menu, 'notices':notices, 'first_notice':first_notice, 'list_notices_count':list_notices_count, 'site':site})

def cart(request):
   return render(request, 'cart.html')
def contacts(request):
   return render(request, 'contacts.html')

def discounts(request):
   return render(request, 'discounts.html')

def products(request):
   products=Product.objects.all()
   for product in products:
      product.price=f"{product.price:.2f}"
      product.old_price=f"{product.old_price:.2f}"

   menu=Menu.objects.first()

   site=Site.objects.first()

   return render(request, 'products.html', {'products':products, 'menu':menu, 'site':site})


def updateItem(request):
   data = json.loads(request.body)
   productId=data['productId']
   action=data['action']

   print(productId)
   print(action)

   #customer = request.user.customer
   product =  Product.objects.get(id=productId)
   return JsonResponse(f'{product.id}', safe=False)

def product(request):
   id = request.GET.get('id', '')
   
   product =  Product.objects.get(id=id)
   product.price=f"{product.price:.2f}"

   #return render(request, 'product.html', {'id':id, 'price':product.price, 'name':product.name})
   menu=Menu.objects.first()

   site=Site.objects.first()

   return render(request, 'product.html', {'product':product,'id':id,'details':product.details, 'price':product.price, 'name':product.name, 'image':product.image.url, 'menu':menu, 'site':site})
