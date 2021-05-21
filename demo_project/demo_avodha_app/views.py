from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import shop
from .forms import modeForm

# Create your views here.
def demo(request):
    product = shop.objects.all()
    return render(request, 'home.html', {'products':product})
def details(request,shop_id):
    product1 = shop.objects.get(id=shop_id)
    return render(request, 'details.html', {'product1':product1})
def add_product(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        img = request.FILES['img']
        pro = shop(name=name, price=price, desc=desc, img=img)
        pro.save()
        return redirect('/')
        # print("product added")

    return render(request, 'add_product.html')

def update(request,id):

    obj = shop.objects.get(id=id)
    form = modeForm(request.POST or None, request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form':form,'obj':obj})

def delete(request,id):

    if request.method == 'POST':
        obj = shop.objects.get(id=id)
        obj.delete()
        return redirect('/')
    return render(request, 'delete.html')