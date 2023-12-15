from django.dispatch import receiver
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from updates.forms import UpdatesForm
from django.core import serializers
from django.urls import reverse
from updates.models import Updates
from book.models import Book
from django.views.decorators.csrf import csrf_exempt
from django.db.models.signals import post_save

@csrf_exempt
def post_update(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")
        author = request.user
        author_username = author.username

        update_entry = Updates(title=title, content=content, author=author, author_username=author_username)
        update_entry.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def get_updates_json(request):
    posts = Updates.objects.filter(author=request.user)
    return HttpResponse(serializers.serialize('json', posts))

def get_updates_json_all(request):
    posts = Updates.objects.all().order_by('-data_added')
    return HttpResponse(serializers.serialize('json', posts))

def show_updates(request):
    user = request.user
    if user.role == 'AUTHOR':
        return render(request, 'updates.html')
    elif user.role == 'READER':
        return render(request, 'updates_user.html')

def show_json(request):
    data = Updates.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def post_delete(request, pk):
    posts = Updates.objects.get(id=pk)
    posts.delete()
    return HttpResponseRedirect('/updates/')

@receiver(post_save, sender=Book)  # Connect to the Book model
def create_update_for_new_book(sender, instance, created, **kwargs):
    if created:
        title = instance.title
        description = instance.description
        author = instance.author

        new_update = Updates(title=title, content=description, author=author)
        new_update.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()