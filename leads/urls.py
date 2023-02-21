from django.urls import path
from . import views


app_name="leads"
urlpatterns = [
    path('', views.ListPageView.as_view(), name='leads'),
    path('<int:pk>', views.LeadDetail.as_view(), name='lead_detail'),
    path('create/', views.CreatLeadView.as_view(), name='lead_create'),
    path('<int:pk>/update/', views.UpdateLead.as_view(), name='lead_update'),
    path('<int:pk>/delete/', views.DeleteLead.as_view(), name='lead_delete'),
]