from django.urls import path
from cadastros.views import home

urlpatterns = [
    path('', home)
]