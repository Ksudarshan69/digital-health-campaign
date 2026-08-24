from django.db import models
from django.urls import reverse


class TeamCategory(models.Model):
    """e.g. Campaign Coordinator, Field Coordinator, Volunteer Members (section 21)."""
    name = models.CharField(max_length=100, unique=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Team Categories"
        ordering = ["display_order", "name"]

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    full_name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=170, unique=True)
    photo = models.ImageField(upload_to="team/", blank=True, null=True)
    position = models.CharField(max_length=150)
    category = models.ForeignKey(TeamCategory, on_delete=models.SET_NULL, null=True, related_name="members")
    district_location = models.CharField(max_length=100, blank=True)
    education = models.CharField(max_length=200, blank=True)
    experience = models.TextField(blank=True)
    skills = models.CharField(max_length=300, blank=True, help_text="Comma-separated")
    responsibilities = models.TextField(blank=True)
    biography = models.TextField(blank=True)

    facebook_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)

    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "full_name"]

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse("team:detail", kwargs={"slug": self.slug})

    def skills_list(self):
        return [s.strip() for s in self.skills.split(",") if s.strip()]
