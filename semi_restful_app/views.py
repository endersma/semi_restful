from django.shortcuts import render, redirect
from .models import Show
# Create your views here.

def index(request):
    context = {
        'shows': Show.objects.all(),
    }
    return render(request, 'shows.html', context)

def show(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show
    }
    return render(request, 'show.html', context)

def new(request):
    return render(request, 'new.html')

def edit(request, show_id):
    show_to_edit = Show.objects.get(id=show_id)
    context = {
        'updated_show': show_to_edit
    }
    return render(request, 'edit.html', context)

def update(request, show_id):
    update_show = Show.objects.get(id=show_id)
    update_show.title = request.POST['title']
    update_show.network = request.POST['network']
    update_show.release_date = request.POST['release_date']
    update_show.description = request.POST['description']
    update_show.save()
    return redirect(f'/shows/{ update_show.id }')

def create(request):
    new_show = Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        release_date=request.POST['release_date'],
        description=request.POST['description'],
    )
    return redirect(f'/shows/{ new_show.id }')

def delete(request, show_id):
    show_to_delete = Show.objects.get(id=show_id)
    show_to_delete.delete()
    return redirect('/shows')