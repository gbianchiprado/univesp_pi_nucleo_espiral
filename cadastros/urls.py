from django.urls import path
from cadastros.views import home, consult

urlpatterns = [
    path('', home),
    path('consulta', consult)

]