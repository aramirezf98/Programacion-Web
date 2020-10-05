from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *


class AgendaView(ListView):
    model = Agenda
    template_name = "base/citas/listar.html"
    context_object_name = "listado"
    queryset = Agenda.objects.filter(estado=False)
    paginate_by = 15

    def get_queryset(self):
        descripcion = self.request.GET.get('descripcion') if self.request.GET.get('descripcion') else ''
        return self.model.objects.filter(paciente__nombre__icontains=descripcion, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descripcion'] = self.request.GET.get('descripcion') if self.request.GET.get('descripcion') else ''
        context['titulo'] = "Consulta de Citas"
        return context


class CrearAgendaView(CreateView):
    model = Agenda
    # fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/citas/form.html"
    form_class = AgendaForm
    success_url = reverse_lazy('base:citas')
    context_object_name = "citas"


class EditarAgendaView(UpdateView):
    model = Agenda
    # fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/citas/form.html"
    form_class = AgendaForm
    success_url = reverse_lazy('base:citas')
    context_object_name = "citas"


class EliminarAgendaView(DeleteView):

    def post(self, request, *args, **kwargs):
        pk = request.POST.get("id")
        filtro = Agenda.objects.get(id=pk)
        filtro.estado = False
        filtro.save()
        return redirect('base:citas')
