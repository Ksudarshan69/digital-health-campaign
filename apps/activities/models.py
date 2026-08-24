from django.db import models
from django.urls import reverse
from apps.campaigns.models import CampaignArea


class Activity(models.Model):
    """A campaign program/event (spec section 19)."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    date = models.DateField()
    location = models.CharField(max_length=200)
    campaign_area = models.ForeignKey(CampaignArea, on_delete=models.SET_NULL, null=True, blank=True, related_name="activities")
    description = models.CharField(max_length=300)
    participant_count = models.PositiveIntegerField(default=0)
    featured_image = models.ImageField(upload_to="activities/", blank=True, null=True)
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("activities:detail", kwargs={"slug": self.slug})


class ActivityImage(models.Model):
    activity = models.ForeignKey(Activity, related_name="gallery_images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="activities/gallery/")
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Image for {self.activity.title}"
