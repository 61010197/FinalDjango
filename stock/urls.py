from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('review',views.review,name='review'),
    path('contact',views.contact,name='contact'),
]

