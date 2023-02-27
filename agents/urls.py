from django.urls import path
from . import views

app_name='agents'
urlpatterns =[
    path('', views.AgentListView.as_view(), name="agent-list"),
    path('create/', views.CreateAgentView.as_view(), name="create-agent"),
    path('<int:pk>/delete', views.DeleteAgentView.as_view(), name="delete-agent"),
    path('<int:pk>/detail', views.DetailAgentView.as_view(), name="agent-detail"),
    path('<int:pk>/update', views.UpdateAgentView.as_view(), name="agent-update")
]