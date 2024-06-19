from django.contrib import admin
from django.urls import path
from . import views
from Cont01.views import home_view, hello_view, input_view, form_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('hello/', hello_view, name='hello'),
    path('sample/input/', input_view, name='input'),
    path('sample/form/', form_view, name='form'),
    path('foobar/', views.foobar_view, name='foobar'), 
]
