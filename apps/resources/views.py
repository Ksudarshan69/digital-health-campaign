from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Resource, ResourceCategory


def resource_list(request):
    resources = Resource.objects.filter(is_published=True)

    query = request.GET.get("q", "").strip()
    if query:
        from django.db.models import Q
        resources = resources.filter(Q(title__icontains=query) | Q(description__icontains=query))

    category_slug = request.GET.get("category")
    if category_slug:
        resources = resources.filter(category__slug=category_slug)

    resource_type = request.GET.get("type")
    if resource_type:
        resources = resources.filter(resource_type=resource_type)

    paginator = Paginator(resources, 12)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(request, "resources/list.html", {
        "page_obj": page_obj,
        "categories": ResourceCategory.objects.all(),
        "resource_types": Resource._meta.get_field("resource_type").choices,
        "query": query,
        "selected_category": category_slug,
        "selected_type": resource_type,
    })


def resource_detail(request, slug):
    resource = get_object_or_404(Resource, slug=slug, is_published=True)
    return render(request, "resources/detail.html", {"resource": resource})
