from django.db import models
from django.urls import reverse

ALBUM_CATEGORY_CHOICES = [
    ("campaign_activities", "Campaign Activities"),
    ("community_programs", "Community Programs"),
    ("training_programs", "Training Programs"),
    ("field_visits", "Field Visits"),
    ("awareness_videos", "Awareness Videos"),
    ("campaign_videos", "Campaign Videos"),
    ("training_videos", "Training Videos"),
    ("interviews", "Interviews"),
]

MEDIA_TYPE_CHOICES = [
    ("photo", "Photo"),
    ("video", "Video"),
]


class GalleryAlbum(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    category = models.CharField(max_length=30, choices=ALBUM_CATEGORY_CHOICES)
    cover_image = models.ImageField(upload_to="gallery/covers/", blank=True, null=True)
    description = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("gallery:album_detail", kwargs={"slug": self.slug})


class GalleryMedia(models.Model):
    album = models.ForeignKey(GalleryAlbum, related_name="media_items", on_delete=models.CASCADE)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES, default="photo")
    image = models.ImageField(upload_to="gallery/media/", blank=True, null=True)
    video_url = models.URLField(blank=True, help_text="Embedded video URL (YouTube etc.), for media_type=video")
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.caption or f"Media in {self.album.title}"
