from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('track/',views.track,name="track"),
    path('contact/',views.contact,name="contact"),
    path('productView/',views.productView,name="productView"),
    path('checkout/',views.checkout,name="checkout"),
]