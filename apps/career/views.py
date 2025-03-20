from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import QuarterForm, LevelForm, CareerForm
from .models import Quarter, Level, Career

# CRUD Views for Quarter
#---------------------------------------------------------------------------------------------------

def quarter_list(request):
    quarters = Quarter.objects.all()
    context = {
        "quarters": quarters
    }
    return render(request, 'career/quarter/index.html', context)

def quarter_create(request):
    if request.method == 'POST':
        form = QuarterForm(request.POST)
        if form.is_valid():
            quarter = Quarter(
                quarter=form.cleaned_data['quarter'],
                quarter_name=form.cleaned_data['quarter_name']
            )
            quarter.save()
            return redirect('career:quarter_list')
    else:
        form = QuarterForm()
        return render(request, 'career/quarter/create.html', {'form': form})
    
def quarter_details(request, q_id):
    quarter = Quarter.objects.get(pk=q_id)
    return render(request, 
                  'career/quarter/details.html',
                  {'quarter': quarter})
    
def quarter_update(request, q_id):
    q = Quarter.objects.get(pk=q_id)
    if request.method == 'POST':
        form = QuarterForm(request.POST)
        if form.is_valid():
            q.quarter = form.cleaned_data['quarter']
            q.quarter_name = form.cleaned_data['quarter_name']
            q.save()
            return redirect('career:quarter_list')
        else:
            return HttpResponse('Hay error en el formulario')
    else:
        form = QuarterForm(instance=q)
        return render(request, 
                    'career/quarter/update.html',
                    {'form': form})
        
def quarter_delete(request, q_id):
    if request.method == 'POST':
        q = Quarter.objects.get(pk=q_id)
        q.delete()
        return redirect('career:quarter_list')
    
#---------------------------------------------------------------------------------------------------
# Vistas basadas en clases para level model
class LevelListView(ListView):
    model = Level
    template_name = 'career/level/index.html'
    context_object_name = 'levels'
    
class LevelDetailView(DetailView):
    model = Level
    template_name = 'career/level/details.html'
    context_object_name = 'level'
    
class LevelCreateView(CreateView):
    model = Level
    form_class = LevelForm
    template_name = 'career/level/create.html'
    success_url = reverse_lazy('career:level_list')
    
class LevelUpdateView(UpdateView):
    model = Level
    form_class = LevelForm
    template_name = 'career/level/update.html'
    success_url = reverse_lazy('career:level_list')

class LevelDeleteView(DeleteView):
    model = Level
    template_name = 'career/level/delete.html'
    success_url = reverse_lazy('career:level_list')

#---------------------------------------------------------------------------------------------------
# Vistas basadas en clases para career model
class CareerListView(ListView):
    model = Career
    template_name = 'career/career/index.html'
    context_object_name = 'careers'
    
class CareerDetailView(DetailView):
    model = Career
    template_name = 'career/career/details.html'
    context_object_name = 'career'
    
class CareerCreateView(CreateView):
    model = Career
    form_class = CareerForm
    template_name = 'career/career/create.html'
    success_url = reverse_lazy('career:career_list')
    
class CareerUpdateView(UpdateView):
    model = Career
    form_class = CareerForm
    template_name = 'career/career/update.html'
    success_url = reverse_lazy('career:career_list')
    
class CareerDeleteView(DeleteView):
    model = Career
    template_name = 'career/career/delete.html'
    success_url = reverse_lazy('career:career_list')