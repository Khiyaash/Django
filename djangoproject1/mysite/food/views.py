from django.shortcuts import render
from django.http import HttpResponse
from .models import Items
from django.template import loader
# Create your views here.
def index(request):
    return HttpResponse('Hello world')

def item(request):
    return HttpResponse('<h1>This is an item view<h1>')

def display_item(request):
    item_list=Items.objects.all()
    #template = loader.get_template('food/index.html')
    context ={ 'item_list': item_list,}
    #return HttpResponse(template.render(context,request))
    return render (request,'food/index.html',context)

def detail(request,item_id):
    item = Items.objects.get(pk=item_id)
    context ={
        'item': item
    }
    return render(request,'food/detail.html',context)
    #return HttpResponse("this is an item no/id :%s" %item_id)
"""
def display_item(request):
    return render(request, 'food/index.html')"""


