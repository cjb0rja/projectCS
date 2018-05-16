from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from vaccine.models import Vaccine
from vaccine.forms import VaccineForm

class IndexView(generic.ListView):
	template_name = 'vaccine/index.html'
