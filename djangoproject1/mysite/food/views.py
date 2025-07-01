from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Items
from django.template import loader
from .forms import ItemForm
from django.views.generic.edit import CreateView
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

def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:display_item')
    return render(request,'food/item-form.html',{'form':form})
#this is a class based view
class CreateItem(CreateView):
    model = Items;
    fields = ['item_name','item_desc','item_price','item_image']
    template_name='food/item-form.html'
    def form_valid(self,form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

def update_item(request,id):
    item = Items.objects.get(pk=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:display_item')
    
    return render(request,'food/item-form.html',{'form':form,'item':item})

def delete_item(request,id):
    item = Items.objects.get(pk=id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:display_item')
    return render(request,'food/item-deleteform.html',{'item':item})
    

"""
def display_item(request):
    return render(request, 'food/index.html')"""


