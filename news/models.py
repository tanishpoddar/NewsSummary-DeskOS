from django.db import models
from django.contrib.auth.models import User

class SavedNews(models.Model):
    """
    Model to store news articles saved by users.
    Each user can save a news article (by URL) only once.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_news')
    title = models.CharField(max_length=512)
    url = models.URLField()
    summary = models.TextField()
    published_at = models.DateTimeField(null=True, blank=True)
    source = models.CharField(max_length=256, blank=True)

    class Meta:
        unique_together = ('user', 'url')
        verbose_name = 'Saved News'
        verbose_name_plural = 'Saved News'

    def __str__(self):
        return self.title
