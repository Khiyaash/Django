from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path('hello/',views.index,name ='index'),
    path('item/',views.item,name='item'),
    path('',views.display_item,name = 'display_item'),
    path('<int:item_id>/',views.detail,name='detail')
]
