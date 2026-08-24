from django.db import models
from django.urls import reverse

RESOURCE_TYPE_CHOICES = [
    ("article", "Article"),
    ("video", "Video"),
    ("poster", "Poster"),
    ("infographic", "Infographic"),
    ("pdf", "PDF"),
]


class ResourceCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)

    class Meta:
        verbose_name_plural = "Resource Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Resource(models.Model):
    """Learning resource — article, video, poster, infographic, or PDF (section 18)."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    thumbnail = models.ImageField(upload_to="resources/thumbnails/", blank=True, null=True)
    category = models.ForeignKey(ResourceCategory, on_delete=models.SET_NULL, null=True, related_name="resources")
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPE_CHOICES)
    description = models.CharField(max_length=300)
    content = models.TextField(blank=True, help_text="Full article body, for type=article")
    file = models.FileField(upload_to="resources/files/", blank=True, null=True, help_text="For PDF, poster, or infographic types")
    external_video_url = models.URLField(blank=True, help_text="For type=video (e.g. YouTube link)")
    author = models.CharField(max_length=120, blank=True)
    published_date = models.DateField()
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("resources:detail", kwargs={"slug": self.slug})
