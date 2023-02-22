from django.contrib import admin
from django.urls import path, include
from leads import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls', namespace="leads")),
    path('agents/', include('agents.urls', namespace="agents")),
    path('', views.LandingPageView.as_view() , name="landing_page"),
    path('login/', LoginView.as_view(), name="login"), 
    path('logout/', LogoutView.as_view(), name="logout"),
    path('signup', views.SignupView.as_view(), name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


