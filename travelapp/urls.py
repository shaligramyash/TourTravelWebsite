from unittest import result
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('qr',views.qrcode, name='qr'),
    path('service',views.services, name='service'),
    path('tour',views.tourpack, name='tour'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact')

]