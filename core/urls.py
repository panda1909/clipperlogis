from django.contrib import admin
from django.urls import path
from core.views import index, contact
urlpatterns = [
    path('', index, name='home'),
    path('contact', contact, name='contact')
]
