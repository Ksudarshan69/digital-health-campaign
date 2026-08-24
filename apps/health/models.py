from django.db import models
from django.urls import reverse

TOOL_CATEGORY_CHOICES = [
    ("monitoring", "Health Monitoring Device"),
    ("telemedicine", "Telemedicine"),
    ("mobile_app", "Mobile Application"),
    ("emergency", "Emergency Information"),
]

PREVENTIVE_CATEGORY_CHOICES = [
    ("ncd", "Non-Communicable Diseases"),
    ("communicable", "Communicable Diseases"),
    ("maternal_child", "Maternal & Child Health"),
    ("mental", "Mental Wellbeing"),
]


class HealthTool(models.Model):
    """Digital health tool/device explainer (spec section 15)."""
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=170, unique=True)
    icon_image = models.ImageField(upload_to="health_tools/", blank=True, null=True)
    short_description = models.CharField(max_length=250)
    detailed_content = models.TextField()
    category = models.CharField(max_length=30, choices=TOOL_CATEGORY_CHOICES)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("health:tool_detail", kwargs={"slug": self.slug})


class PreventiveHealthTopic(models.Model):
    """Preventive-health education topic (spec section 16)."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    category = models.CharField(max_length=30, choices=PREVENTIVE_CATEGORY_CHOICES)
    featured_image = models.ImageField(upload_to="preventive_health/", blank=True, null=True)
    summary = models.CharField(max_length=300)
    detailed_content = models.TextField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["category", "title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("health:preventive_detail", kwargs={"slug": self.slug})
