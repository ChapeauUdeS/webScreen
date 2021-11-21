from django.urls import path

from . import views

urlpatterns = {
    path('', views.index, name='index'),
    path('ajax/sendCommand/<str:cmd>', views.sendCommand, name='sendCommand')
}
