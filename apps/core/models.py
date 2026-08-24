from django.db import models


class CampaignSettings(models.Model):
    """
    Singleton model holding site-wide values (section 25 of the spec) so
    templates never hard-code the campaign name, logo, socials, etc.
    Only one row should ever exist - enforced by save().
    """
    campaign_name = models.CharField(max_length=200, default="Digital Health Awareness Campaign")
    slogan = models.CharField(max_length=200, default="Digital Knowledge for a Healthier Nepal")
    logo = models.ImageField(upload_to="branding/", blank=True, null=True)

    hero_title = models.CharField(max_length=200, blank=True)
    hero_description = models.TextField(blank=True)
    mission = models.TextField(blank=True)
    introduction = models.TextField(blank=True)

    contact_address = models.CharField(max_length=255, blank=True)
    contact_phone = models.CharField(max_length=50, blank=True)
    contact_email = models.EmailField(blank=True)

    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)

    # Homepage statistics (section 8) - simple integers, editable in admin
    stat_districts = models.PositiveIntegerField(default=0)
    stat_people_reached = models.PositiveIntegerField(default=0)
    stat_programs = models.PositiveIntegerField(default=0)
    stat_volunteers = models.PositiveIntegerField(default=0)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Campaign Settings"
        verbose_name_plural = "Campaign Settings"

    def __str__(self):
        return self.campaign_name

    def save(self, *args, **kwargs):
        self.pk = 1  # enforce singleton
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
