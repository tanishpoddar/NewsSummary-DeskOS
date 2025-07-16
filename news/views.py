from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .utils import fetch_latest_news, fetch_news_by_query, summarize_text
from .serializers import SummarizedNewsSerializer, SavedNewsSerializer
from .models import SavedNews
from django.http import HttpResponse
from django.conf import settings
from django.http import FileResponse
import os

class UserRegistrationView(generics.CreateAPIView):
    """
    API endpoint for user registration.
    """
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

class LatestNewsView(APIView):
    """
    API endpoint to fetch and summarize the latest news articles.
    Requires authentication.
    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        articles = fetch_latest_news()
        summarized = []
        for article in articles:
            text = article.get('content') or article.get('description') or article.get('title', '')
            summary = summarize_text(text)
            summarized.append({
                'title': article.get('title'),
                'url': article.get('url'),
                'summary': summary,
                'published_at': article.get('publishedAt'),
                'source': article.get('source', {}).get('name', ''),
            })
        return Response(SummarizedNewsSerializer(summarized, many=True).data)

class SearchNewsView(APIView):
    """
    API endpoint to search and summarize news articles by query.
    Requires authentication.
    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        query = request.query_params.get('q')
        if not query:
            return Response({'error': 'Query parameter "q" is required.'}, status=400)
        articles = fetch_news_by_query(query)
        summarized = []
        for article in articles:
            text = article.get('content') or article.get('description') or article.get('title', '')
            summary = summarize_text(text)
            summarized.append({
                'title': article.get('title'),
                'url': article.get('url'),
                'summary': summary,
                'published_at': article.get('publishedAt'),
                'source': article.get('source', {}).get('name', ''),
            })
        return Response(SummarizedNewsSerializer(summarized, many=True).data)

class SaveNewsView(APIView):
    """
    API endpoint to save a news article for the authenticated user.
    Prevents duplicate saves for the same user and URL.
    """
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = SavedNewsSerializer(data=request.data)
        if serializer.is_valid():
            # Prevent duplicate save for same user and url
            if SavedNews.objects.filter(user=request.user, url=serializer.validated_data['url']).exists():
                return Response({'detail': 'You have already saved this news article.'}, status=400)
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class SavedNewsListView(APIView):
    """
    API endpoint to list all news articles saved by the authenticated user.
    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        saved = SavedNews.objects.filter(user=request.user)
        serializer = SavedNewsSerializer(saved, many=True)
        return Response(serializer.data)

def api_root(request):
    """
    Serves the main static HTML file for the frontend SPA.
    """
    static_path = os.path.join(settings.BASE_DIR, 'newsapi_project', 'static', 'index.html')
    return FileResponse(open(static_path, 'rb'), content_type='text/html')
