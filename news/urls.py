"""
URL routing for the news app. Includes authentication and news-related endpoints.
"""
from django.urls import path
from .views import (
    UserRegistrationView,
    LatestNewsView,
    SearchNewsView,
    SaveNewsView,
    SavedNewsListView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('auth/register/', UserRegistrationView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += [
    path('news/latest/', LatestNewsView.as_view(), name='news-latest'),
    path('news/search/', SearchNewsView.as_view(), name='news-search'),
    path('news/save/', SaveNewsView.as_view(), name='news-save'),
    path('news/saved/', SavedNewsListView.as_view(), name='news-saved'),
] 