from django.urls import path,include
from principal import views



urlpatterns = [
    path('',views.principal, name='principal'),
    # path('cad/',include('cadastros.urls')),
]