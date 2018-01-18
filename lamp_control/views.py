from django.shortcuts import render
from django.views.generic import ListView

from lamp_control.models import Lamp


class ListLamps(ListView):
    model = Lamp
    template = "list_lamps.html"
