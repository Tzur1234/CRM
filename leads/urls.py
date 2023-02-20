from django.urls import path
from . import views


app_name="leads"
urlpatterns = [
    path('', views.ListPageView.as_view(), name='leads'),
    path('<int:pk>', views.LeadDetail.as_view(), name='lead_detail'),
    path('create/', views.create, name='lead_create'),
    path('<int:pk>/update/', views.update, name='lead_update'),
    path('<int:pk>/delete/', views.delete, name='lead_delete'),
]