from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import VolunteerApplicationForm


def join(request):
    if request.method == "POST":
        form = VolunteerApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for applying! Our team will review your application and get in touch soon.")
            return redirect("volunteers:join")
    else:
        form = VolunteerApplicationForm()
    return render(request, "volunteers/join.html", {"form": form})
