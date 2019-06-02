from django.shortcuts import render
from .models import SuperNinja
from django.http import HttpResponse
import random
import json


def ninja_details_view(request):
    obj = SuperNinja.objects.get(id=random.randint(1, 30))
    context = {
        'name': obj.name,
        'agility': obj.agility,
        'strength': obj.strength,
        'intelligence': obj.intelligence,
        'vitality': obj.vitality,
        'katana': obj.katana,
        'titre': 'Ninja picker'
    }
    return render(request, 'home.html', context)




