from django import forms
from .models import VolunteerApplication


class VolunteerApplicationForm(forms.ModelForm):
    class Meta:
        model = VolunteerApplication
        fields = ["full_name", "age", "gender", "district", "education", "phone_number",
                  "email", "skills", "previous_experience", "motivation"]
        widgets = {
            "previous_experience": forms.Textarea(attrs={"rows": 3}),
            "motivation": forms.Textarea(attrs={"rows": 4}),
        }
