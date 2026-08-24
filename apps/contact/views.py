from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactMessageForm


def contact_form(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent. We'll get back to you soon.")
            return redirect("contact:form")
    else:
        form = ContactMessageForm()
    return render(request, "contact/form.html", {"form": form})
