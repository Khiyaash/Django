from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path('hello/',views.index,name ='index'),
    path('item/',views.item,name='item'),
    path('',views.display_item,name = 'display_item'),
    path('<int:item_id>/',views.detail,name='detail'),
    #add items
    path('add',views.CreateItem.as_view(),name='create_item'),
    #update items
    path('update/<int:id>/',views.update_item,name='update_item'),
    path('delete/<int:id>/',views.delete_item,name='delete_item')
]
