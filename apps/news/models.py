from django.db import models
from django.urls import reverse

NEWS_CATEGORY_CHOICES = [
    ("campaign_news", "Campaign News"),
    ("announcements", "Announcements"),
    ("upcoming_events", "Upcoming Events"),
    ("health_awareness", "Health Awareness"),
    ("program_updates", "Program Updates"),
]


class NewsPost(models.Model):
    """News & updates article (spec section 20)."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    category = models.CharField(max_length=30, choices=NEWS_CATEGORY_CHOICES)
    featured_image = models.ImageField(upload_to="news/", blank=True, null=True)
    summary = models.CharField(max_length=300)
    content = models.TextField()
    author = models.CharField(max_length=120, blank=True)
    published_date = models.DateField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news:detail", kwargs={"slug": self.slug})
