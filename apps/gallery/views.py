from django.shortcuts import render, get_object_or_404
from .models import GalleryAlbum


def album_list(request):
    albums = GalleryAlbum.objects.all()
    category = request.GET.get("category")
    if category:
        albums = albums.filter(category=category)
    return render(request, "gallery/list.html", {
        "albums": albums,
        "categories": GalleryAlbum._meta.get_field("category").choices,
        "selected_category": category,
    })


def album_detail(request, slug):
    album = get_object_or_404(GalleryAlbum, slug=slug)
    return render(request, "gallery/detail.html", {"album": album})
