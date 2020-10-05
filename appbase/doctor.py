from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *


class DoctorView(ListView):
    model = Doctor
    template_name = "base/doctor/doctor.html"
    context_object_name = "doctores"
    queryset = Doctor.objects.filter(estado=False)
    paginate_by = 15

    def get_queryset(self):
        nombre = self.request.GET.get(
            'nombre') if self.request.GET.get('nombre') else ''
        return self.model.objects.filter(nombre__icontains=nombre, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'nombre') if self.request.GET.get('nombre') else ''
        context['titulo'] = "Consulta de Doctor"
        return context


class CrearDoctorView(CreateView):
    model = Doctor
    # fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/doctor/form_doctor.html"
    form_class = DoctorForm
    success_url = reverse_lazy('base:doctor')
    context_object_name = "doctor"


class EditarDoctorView(UpdateView):
    model = Doctor
    # fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/doctor/form_doctor.html"
    form_class = DoctorForm
    success_url = reverse_lazy('base:doctor')
    context_object_name = "doctor"


class EliminarDoctorView(DeleteView):

    def post(self, request, *args, **kwargs):
        pk = request.POST.get("id")
        filtro = Doctor.objects.get(id=pk)
        filtro.estado = False
        filtro.save()
        return redirect('base:doctor')
