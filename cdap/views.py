from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Locacion, Empresa, Persona


#class IndexView(generic.ListView):
#    template_name = 'cdap/index.html'
#    context_object_name = 'latest_persona_list'
#
#    def get_queryset(self):
#        """Return the last five published questions."""
#        return Question.objects.order_by('-pub_date')[:5]


# Listview
class PersonaList(generic.ListView):
    model = Persona
    template_name = 'cdap/persona_list.html'
    def get_queryset(self):
        queryset = super(PersonaList, self).get_queryset()
        return queryset.filter(activo=True)

class LocacionList(generic.ListView):
    model = Locacion
    template_name = 'cdap/locacion_list.html'

class EmpresaList(generic.ListView):
    model = Empresa
    template_name = 'cdap/empresa_list.html'


# DetailView
class LocacionDetail(generic.DetailView):
    model = Locacion
    template_name = 'cdap/locacion.html'

class EmpresaDetail(generic.DetailView):
    model = Empresa
    template_name = 'cdap/empresa.html'

class PersonaDetail(generic.DetailView):
    model = Persona
    template_name = 'cdap/persona.html'
