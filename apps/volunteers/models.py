from django.db import models

GENDER_CHOICES = [
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other"),
    ("prefer_not_to_say", "Prefer not to say"),
]

STATUS_CHOICES = [
    ("pending", "Pending"),
    ("reviewed", "Reviewed"),
    ("accepted", "Accepted"),
    ("rejected", "Rejected"),
]


class VolunteerApplication(models.Model):
    """Volunteer registration submission (spec section 23)."""
    full_name = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True)
    district = models.CharField(max_length=100)
    education = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField()
    skills = models.CharField(max_length=300, blank=True)
    previous_experience = models.TextField(blank=True)
    motivation = models.TextField(verbose_name="Why do you want to join?")

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-submitted_at"]

    def __str__(self):
        return f"{self.full_name} ({self.get_status_display()})"
