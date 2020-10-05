from django.contrib import admin
from appbase.models import (Paciente, Sintoma, Diagnostico,
                            EstudioGabinete, Medicamento, Dosis, Frecuencia,
                            Duracion, SignoVital, Antecedente, GrupoAntecedente,
                            Provincia, Ciudad, Profesion, Titulo, Sangre, Horario, Doctor, Agenda)


class AgendaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'fecha', 'hora', 'motivo', 'estado')

    ordering = ('fecha',)
    search_fields = ('paciente', 'fecha')
    list_filter = ('paciente__apellido', 'fecha')


admin.site.register(Paciente)
admin.site.register(Sintoma)
admin.site.register(Diagnostico)
admin.site.register(EstudioGabinete)
admin.site.register(Medicamento)
admin.site.register(Dosis)
admin.site.register(Frecuencia)
admin.site.register(Duracion)
admin.site.register(SignoVital)
admin.site.register(GrupoAntecedente)
admin.site.register(Antecedente)
admin.site.register(Provincia)
admin.site.register(Ciudad)
admin.site.register(Profesion)
admin.site.register(Titulo)
admin.site.register(Sangre)
admin.site.register(Horario)
admin.site.register(Doctor)
admin.site.register(Agenda, AgendaAdmin)
