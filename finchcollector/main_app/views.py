from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Finch, Tree
from .forms import FeedingForm

class FinchCreate(LoginRequiredMixin, CreateView):
    model = Finch
    fields = ['name', 'species', 'description', 'age']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class FinchUpdate(LoginRequiredMixin, UpdateView):
    model = Finch
    fields = ['species', 'description', 'age']

class FinchDelete(LoginRequiredMixin, DeleteView):
    model = Finch
    success_url = '/finches/'

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def finches_index(request):
    finches = Finch.objects.filter(user=request.user)
    return render(request, 'finches/index.html', {'finches' : finches})

@login_required
def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    trees_finch_doesnt_live_in = Tree.objects.exclude(id__in = finch.trees.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch,
        'feeding_form': feeding_form,
        'trees': trees_finch_doesnt_live_in })

@login_required
def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

@login_required
def assoc_tree(request, finch_id, tree_id):
    Finch.objects.get(id=finch_id).trees.add(tree_id)
    return redirect('detail', finch_id=finch_id)

@login_required
def unassoc_tree(request, cat_id, toy_id):
  Finch.objects.get(id=cat_id).trees.remove(tree_id)
  return redirect('detail', cat_id=cat_id)

class TreeList(LoginRequiredMixin, ListView):
  model = Tree

class TreeDetail(LoginRequiredMixin, DetailView):
  model = Tree

class TreeCreate(LoginRequiredMixin, CreateView):
  model = Tree
  fields = '__all__'

class TreeUpdate(LoginRequiredMixin, UpdateView):
  model = Tree
  fields = ['name', 'height']

class TreeDelete(LoginRequiredMixin, DeleteView):
  model = Tree
  success_url = '/trees/'    


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)