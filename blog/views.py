from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from .models import Post
from .forms import PostForm


def is_staff(user):
    return user.is_authenticated and user.is_staff


# ───────────────────────────────────────
# PÚBLICO
# ───────────────────────────────────────
def post_list(request):
    query = request.GET.get("search", "").strip()
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(category__name__icontains=query)
        )
    else:
        posts = Post.objects.all()
    return render(request, "blog/post_list.html",
                  {"posts": posts.order_by("-created"), "search": query})


def post_detail(request, post_id):
    """Vista pública de detalle (opcional, pero útil)."""
    post = get_object_or_404(Post, id=post_id)
    return render(request, "blog/post_detail.html", {"post": post})


# ───────────────────────────────────────
# CRUD (STAFF)
# ───────────────────────────────────────
@user_passes_test(is_staff)
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Publicación creada correctamente.")
            return redirect("blog:post_list")
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form})


@user_passes_test(is_staff)
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Publicación actualizada correctamente.")
            return redirect("blog:post_list")
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_form.html", {"form": form})


@user_passes_test(is_staff)
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Publicación eliminada correctamente.")
        return redirect("blog:post_list")
    return render(request, "blog/post_confirm_delete.html", {"post": post})

