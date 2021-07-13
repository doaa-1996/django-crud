from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Snack
from django.urls import reverse_lazy

class HomeView(TemplateView):
  template_name='home.html'

class SnackView(ListView):
    template_name='snacks.html'
    model=Snack


class SnackDetailsView(DetailView):
    template_name = 'snack_details.html'
    model = Snack 



class SnackCreateView(CreateView):
  template_name='snack_create.html'
  model=Snack
  fields=['name','purchaser','desc']    


class SnackUpdateView(UpdateView):
  template_name='snack_update.html'
  model=Snack
  fields=['name','purchaser','desc']    

class SnackDeleteView(DeleteView):
  template_name='snack_delete.html'
  model=Snack
  success_url=reverse_lazy('Snacks')
    