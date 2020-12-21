from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render_to_response
from tagging.fields import Tag
from tagging.models import TaggedItem
from blog.models import BlogPost


def articles(request):
    tags = Tag.objects.usage_for_model(BlogPost, counts=True, filters={'visible': True})
    posts = BlogPost.objects.filter(visible=True).order_by('-published')[0:10]
    recent = posts[0:5]
    return render_to_response('article.htm', {'tags': tags, 'posts': posts, 'listview': True, 'recent': recent})


def post_url(request, post_url):
    tags = Tag.objects.usage_for_model(BlogPost, counts=True, filters={'visible': True})
    posts = BlogPost.objects.filter(url=post_url, visible=True)
    if posts.count() < 1:
        raise Http404
    description = posts[0].meta_description
    title = posts[0].title
    recent = BlogPost.objects.filter(visible=True).order_by('-published')[0:5]
    return render_to_response('article.htm', {'tags': tags, 'posts': posts, 'description': description, 'title': title, 'recent': recent})


def article_category(request, category):
    try:
        tag = Tag.objects.get(name=category)
    except ObjectDoesNotExist:
        raise Http404
    posts = TaggedItem.objects.get_by_model(BlogPost, tag).filter(visible=True).order_by('-post_time')
    tags = Tag.objects.usage_for_model(BlogPost, counts=True, filters={'visible': True})
    if posts.count() < 1:
        raise Http404
    recent = BlogPost.objects.filter(visible=True).order_by('-published')[0:5]
    return render_to_response('article.htm', {'tags': tags, 'posts': posts, 'category': category, 'listview': True, 'recent': recent})
