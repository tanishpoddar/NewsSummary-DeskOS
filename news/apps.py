from django.apps import AppConfig


class NewsConfig(AppConfig):
    """
    App configuration for the news app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'
