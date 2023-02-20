from django.urls import path
from . import views


app_name="leads"
urlpatterns = [
    path('', views.lead_list, name='leads'),
    path('<int:pk>', views.lead_detail, name='lead_detail'),
    path('create/', views.create, name='lead_create')
]