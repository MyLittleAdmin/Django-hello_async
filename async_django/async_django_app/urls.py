from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('do_async_thins', views.do_async, name='do_async')
]
