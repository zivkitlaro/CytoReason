from django.shortcuts import render, get_object_or_404
from .models import GeneInfo, Converter, Alias, Ensembl, Entrez

def convert(request):
    c = Converter()
    results, score = c.convert_symbol('a1bg')

    return render(request, 'genemapper/convert/input.html', {'score': score, 'results': results})

