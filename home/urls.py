from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello.as_view(), name='home_page')
]
