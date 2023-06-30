from django.shortcuts import render
from .models import items

def products_page(request):
    Items = items.objects.all()
    return render(request, 'main.html',{'items':Items})