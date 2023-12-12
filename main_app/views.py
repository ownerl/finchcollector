from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch, Creator
from .forms import FeedingForm

# Class Based View
class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['color', 'description', 'favourite_anime']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })

def finch_show(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    feeding_form = FeedingForm()
    id_list = finch.creator_set.all().values_list('id')
    creators_finch_aint_got = Creator.objects.exclude(id__in=id_list)
    return render(request, 'finches/show.html', {
        'finch': finch,
        'feeding_form': feeding_form,
        'creators': creators_finch_aint_got
    })

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('show', finch_id=finch_id)

def associate_creator(request, finch_id, creator_id):
    Finch.objects.get(id=finch_id).creator_set.add(creator_id)
    return redirect('show', finch_id=finch_id)