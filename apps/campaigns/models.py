from django.db import models
from django.urls import reverse

PROVINCE_CHOICES = [
    ("koshi", "Koshi"),
    ("madhesh", "Madhesh"),
    ("bagmati", "Bagmati"),
    ("gandaki", "Gandaki"),
    ("lumbini", "Lumbini"),
    ("karnali", "Karnali"),
    ("sudurpashchim", "Sudurpashchim"),
]

STATUS_CHOICES = [
    ("planned", "Planned"),
    ("active", "Active"),
    ("completed", "Completed"),
]


class CampaignArea(models.Model):
    """A district where the campaign runs (spec section 13)."""
    district_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True)
    province = models.CharField(max_length=30, choices=PROVINCE_CHOICES)
    geographic_region = models.CharField(max_length=100, blank=True, help_text="e.g. Karnali hills, Mid-western Nepal")

    description = models.TextField()
    estimated_population = models.PositiveIntegerField(blank=True, null=True)
    healthcare_situation = models.TextField(blank=True)
    internet_mobile_situation = models.TextField(blank=True)
    major_health_challenges = models.TextField(blank=True)
    digital_health_needs = models.TextField(blank=True)
    campaign_activities_summary = models.TextField(blank=True)

    featured_image = models.ImageField(upload_to="campaign_areas/", blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="planned")

    # Rough centroid, used to place a marker on the districts overview page
    map_x = models.FloatField(blank=True, null=True, help_text="X position (0-100) on the districts overview")
    map_y = models.FloatField(blank=True, null=True, help_text="Y position (0-100) on the districts overview")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["district_name"]
        verbose_name = "Campaign Area"
        verbose_name_plural = "Campaign Areas"

    def __str__(self):
        return self.district_name

    def get_absolute_url(self):
        return reverse("campaigns:detail", kwargs={"slug": self.slug})


class CampaignAreaImage(models.Model):
    """Extra gallery images for a campaign area."""
    area = models.ForeignKey(CampaignArea, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="campaign_areas/gallery/")
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Image for {self.area.district_name}"
