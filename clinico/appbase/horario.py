from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *

DIA_SEMANA = ((0, 'Domingo'), (1, 'Lunes'), (2, 'Martes'),
              (3, 'Miercoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sabado'))

class HorarioView(ListView):
    model = Horario
    template_name = "base/horarios/listar.html"
    context_object_name = "listado"
    queryset = Horario.objects.filter(estado=False)
    paginate_by = 15

    def get_queryset(self):
        dia = self.request.GET.get('dia') if self.request.GET.get('dia') else ''
        return self.model.objects.filter(dia__icontains=dia, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dia'] = self.request.GET.get('dia') if self.request.GET.get('dia') else ''
        context['titulo'] = "Consulta de Horarios"
        context['DIA_SEMANA'] = DIA_SEMANA
        return context


class CrearHorarioView(CreateView):
    model = Horario
    # fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/horarios/form.html"
    form_class = HorarioForm
    success_url = reverse_lazy('base:horario')
    context_object_name = "horario"


class EditarHorarioView(UpdateView):
    model = Horario
    # fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/horarios/form.html"
    form_class = HorarioForm
    success_url = reverse_lazy('base:horario')
    context_object_name = "horario"


class EliminarHorarioView(DeleteView):

    def post(self, request, *args, **kwargs):
        pk = request.POST.get("id")
        filtro = Horario.objects.get(id=pk)
        filtro.estado = False
        filtro.save()
        return redirect('base:horario')
