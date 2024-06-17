from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.input_view, name='input'),
    path('form/', views.form_view, name='form'),
]