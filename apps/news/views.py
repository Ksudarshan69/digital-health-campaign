from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import NewsPost


def news_list(request):
    posts = NewsPost.objects.filter(is_published=True)

    query = request.GET.get("q", "").strip()
    if query:
        from django.db.models import Q
        posts = posts.filter(Q(title__icontains=query) | Q(summary__icontains=query))

    category = request.GET.get("category")
    if category:
        posts = posts.filter(category=category)

    paginator = Paginator(posts, 9)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(request, "news/list.html", {
        "page_obj": page_obj,
        "categories": NewsPost._meta.get_field("category").choices,
        "query": query,
        "selected_category": category,
    })


def news_detail(request, slug):
    post = get_object_or_404(NewsPost, slug=slug, is_published=True)
    related = NewsPost.objects.filter(category=post.category, is_published=True).exclude(pk=post.pk)[:3]
    return render(request, "news/detail.html", {"post": post, "related": related})
