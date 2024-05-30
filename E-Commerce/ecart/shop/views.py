from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Orders,OrderUpdate
from math import ceil
import json

def index(request):
    # products=Product.objects.all()
    # n=len(products)
    # nSlide=n//4 + ceil(n/4 - n//4)
    # allProducts=[[products,nSlide,range(1,nSlide)],[products,nSlide,range(1,nSlide)]]
    allProducts=[]
    catProd=Product.objects.values('category')
    # print(catProd)
    cats={item['category'] for item in catProd}
    # print(cats)
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlide = n // 4 + ceil(n / 4 - n // 4)
        allProducts.append([prod,nSlide,range(1,nSlide)])
    param={'allProducts':allProducts}
    # param={'product':products,'no_of_slides':nSlide,'range':range(1,nSlide)}
    return render(request, 'shop/index.html',param)

def about(request):
    return render(request, 'shop/about.html')
def track(request):
    if request.method=='POST':
        orderId = request.POST.get('orderId','')
        email = request.POST.get('email','')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if(len(order)>0):
                update=OrderUpdate.objects.filter(order_id=orderId)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response = json.dumps([updates,order[0].order_json],default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request, 'shop/Track.html')

def checkout(request):
    if request.method=='POST':
        order_json=request.POST.get('order_json','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        name=request.POST.get('name','')
        add1=request.POST.get('add1','')
        add2=request.POST.get('add2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip_code','')
        order=Orders(order_json=order_json,email=email,phone=phone,name=name,add1=add1,add2=add2,city=city,state=state,zip_code=zip_code)
        order.save()
        update=OrderUpdate(order_id=order.order_id,update_desc="The Order Has Been Placed")
        update.save()
        thank=True
        id=order.order_id
        return render(request,'shop/checkout.html',{'thank':thank,'id':id})
    return render(request,'shop/checkout.html')
def contact(request):
    thank=False
    if request.method=='POST':
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        message=Contact(name=name,email=email,phone=phone,desc=desc)
        message.save()
        thank = True
    return render(request, 'shop/contact.html',{'thank':thank})

def productView(request):
    prod_id=request.GET.get('id')
    products=Product.objects.filter(id=prod_id)
    param={'product':products[0],'id':prod_id}
    return render(request,'shop/productview.html',param)
