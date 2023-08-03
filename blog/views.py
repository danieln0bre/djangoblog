from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

all_posts = [
    {
        "slug": "test",
        "image": "comments-python.jpg",
        "author": "Django admin",
        "date": date(2021, 5, 5),
        "title": "Post title",
        "excerpt": "Example text blablabla",
        "content": """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Autem eos impedit
            laborum magnam molestias praesentium, sed. Excepturi molestiae, necessitatibus
            odit quo similique totam vitae. At delectus fugiat omnis ratione sequi!"""
    },
    {
        "slug": "test2",
        "image": "Firefox_wallpaper.png",
        "author": "Django admin",
        "date": date(2023, 8, 3),
        "title": "Post title2",
        "excerpt": "Example text blablabla2",
        "content": """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Autem eos impedit
            laborum magnam molestias praesentium, sed. Excepturi molestiae, necessitatibus
            odit quo similique totam vitae. At delectus fugiat omnis ratione sequi!"""
    },
    {
        "slug": "test3",
        "image": "wallpaperflare.com_wallpaper.jpg",
        "author": "Django admin",
        "date": date(2022, 3, 3),
        "title": "Post title3",
        "excerpt": "Example text blablabla3",
        "content": """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Autem eos impedit
            laborum magnam molestias praesentium, sed. Excepturi molestiae, necessitatibus
            odit quo similique totam vitae. At delectus fugiat omnis ratione sequi!"""
    }
]


def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts,
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
    })
