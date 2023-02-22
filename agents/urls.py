from django.urls import path
from . import views

app_name='agents'
urlpatterns =[
    path('', views.AgentListView.as_view(), name="agent-list"),
    path('create/', views.CreateAgentView.as_view(), name="create-agent"),
    path('<int:pk>/delete', views.DeleteAgentView.as_view(), name="delete-agent")
]