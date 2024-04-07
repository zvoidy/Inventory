from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='home'),

    path('add', views.add, name='add'),
    path('add_item/', views.add_item, name='add_item'),

    path('sell', views.sell, name='sell'),
    path('sell_item', views.sell_item, name='sell_item'),

    path('update', views.update, name='update'),
    path('update_item', views.update_item, name='update_item'),

    path('remove', views.remove, name='remove'),
    path('remove_item', views.remove_item, name='remove_item'),

    path('transac', views.transac, name='transac'),

    path('display', views.display, name='display'),
    ]

