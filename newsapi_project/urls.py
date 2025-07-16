"""
Root URL configuration for the newsapi_project Django project.
Includes the API routes and the frontend SPA entrypoint.
"""
from django.urls import path, include
from news.views import api_root

urlpatterns = [
    path('', api_root, name='api-root'),  # Serves the frontend SPA
    path('api/', include('news.urls')),
]
