from math import prod
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
import json 

total_money=0

cart_dict={}

GLOBAL_Entry = None
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

    return render(request, 'index.html', {'products':products, 'menu':menu, 'notices':notices, 'first_notice':first_notice, 'list_notices_count':list_notices_count, 'site':site,'total_money':total_money })

def cart(request):
    
    products=Product.objects.all()
    for product in products:
       product.price=f"{product.price:.2f}"
       product.old_price=f"{product.old_price:.2f}"
    ordered_products=[]
    for product in products:
       if product.name in cart_dict:
          ordered_products.append(product)
    menu=Menu.objects.first()

    notices=Notice.objects.all()

    first_notice=Notice.objects.first()

    list_notices_count=[]

    notices_count=len(notices)
        
    for i in range(1, notices_count):
       list_notices_count.append(i)

    site=Site.objects.first()

    return render(request, 'cart.html', {'products':ordered_products,'cart':cart_dict, 'menu':menu, 'notices':notices, 'first_notice':first_notice, 'list_notices_count':list_notices_count, 'site':site,'total_money':total_money })

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

   return render(request, 'products.html', {'products':products, 'menu':menu, 'site':site,'total_money':total_money })



def product(request):
   id = request.GET.get('id', '')
   
   product =  Product.objects.get(id=id)
   product.price=f"{product.price:.2f}"

   #return render(request, 'product.html', {'id':id, 'price':product.price, 'name':product.name})
   menu=Menu.objects.first()

   site=Site.objects.first()

   return render(request, 'product.html', {'product':product,'id':id,'details':product.details, 'price':product.price, 'name':product.name, 'image':product.image.url, 'menu':menu, 'site':site,'total_money':total_money })

def updateItem(request):
   data = json.loads(request.body)
   productId=data['productId']
   action=data['action']

   print(productId)
   print(action)

   #customer = request.user.customer
   product =  Product.objects.get(id=productId)
   return JsonResponse(f'{product.id}', safe=False)

def add_to_cart(request):
   global total_money, cart_dict
   data = json.loads(request.body)
   productId=data['productId']
   action=data['action']

   print(productId)
   print(action)

   #customer = request.user.customer
   product =  Product.objects.get(id=productId)
   
   total_money+= product.price
   if product.name in cart_dict:
      cart_dict[product.name]+=1
   else:
      cart_dict[product.name]=1
   print(cart_dict)
   return JsonResponse(f'{cart_dict}', safe=False)


def checkout(request):
   global total_money, cart_dict
   cart_dict={}
   total_money=0
   #name = request.POST['name_2']
   return render(request, 'checkout.html')
   #for i in range(len(products)):
      #cart_checkout[]

