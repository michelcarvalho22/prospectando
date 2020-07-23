from django.urls import path,include
from accounts import views

urlpatterns = [
    path('',views.registro, name='registro'),
    path('registro/sucesso' ,views.registro_sucesso, name='registro_sucesso'),
    path('ativar/<token>',views.user_active, name='user_active'),
    path('recuperar/',views.recupera_conta, name='recupera_conta'),
    path('recuperar/<id>/<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}', views.create_new_password, name='create_new_password'),
    path('users_viewers', views.users_viewers_list,name='users_viewers_list'),
    path('inclui_vendedor',views.register_viewer,name='register_viewer'),
    path('inclui_vendedor/<int:pk>',views.edit_viewer,name='edit_viewer'),
    path('reset_password/<int:pk>',views.reset_password,name='reset_password'),
]