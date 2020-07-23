from django.urls import path,include
from cadastros import views




urlpatterns = [
    # Leads
    path('leads/',views.leads_lista,name='leads_lista'),
    path('leads/inserir',views.cria_lead,name='cria_lead'),
    path('leads/inserir/<int:pk>',views.edit_lead,name='edit_lead'),
    path('leads/apagar/<int:pk>',views.delete_lead,name='delete_lead'),
    # Status prospeccção
    path('status/',views.status_lista,name='status_lista'),
    path('status/inserir',views.cria_status,name='cria_status'),
    path('status/inserir/<int:pk>',views.edit_status,name='edit_status'),
    path('status/apagar/<int:pk>',views.delete_status,name='delete_status'),
    # Fluxo de Prospecção
    path('fluxo/',views.fluxo_lista,name='fluxo_lista'),
    # path('fluxo/inserir',views.cria_fluxo,name='cria_fluxo'),
    # path('fluxo/inserir/<int:pk>',views.edit_fluxo,name='edit_fluxo'),
    # path('fluxo/apagar/<int:pk>',views.delete_fluxo,name='delete_fluxo'),
]


