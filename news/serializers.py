from django.contrib.auth.models import User
from rest_framework import serializers
from .models import SavedNews

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration. Handles creation of new users.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

class SummarizedNewsSerializer(serializers.Serializer):
    """
    Serializer for summarized news articles.
    """
    title = serializers.CharField()
    url = serializers.URLField()
    summary = serializers.CharField()
    published_at = serializers.DateTimeField(allow_null=True, required=False)
    source = serializers.CharField(allow_blank=True, required=False)

class SavedNewsSerializer(serializers.ModelSerializer):
    """
    Serializer for news articles saved by users.
    """
    class Meta:
        model = SavedNews
        fields = ['id', 'title', 'url', 'summary', 'published_at', 'source'] 