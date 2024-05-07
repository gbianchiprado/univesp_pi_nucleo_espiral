from django.urls import path
from cadastros.views import home, consult, ap_input, closing, pending_docs

urlpatterns = [
    path('', home),
    path('consulta', consult),
    path('lancamento', ap_input),
    path('fechamento', closing),
    path('documentospendentes', pending_docs)

]