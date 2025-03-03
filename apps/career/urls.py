from django.urls import path
from . import views

app_name = 'career'
urlpatterns = [
    path('quarter/', views.quarter_list, name='quarter_list'),
    path('quarter/create/', views.quarter_create, name='quarter_create'),
    path('quarter/<int:q_id>/details/', views.quarter_details, name='quarter_details'),
    path('quarter/<int:q_id>/update/', views.quarter_update, name='quarter_update'),
    path('quarter/<int:q_id>/delete/', views.quarter_delete, name='quarter_delete'),
]
