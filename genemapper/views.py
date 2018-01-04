from .models import GeneInfo, Converter, Alias, Ensembl, Entrez
from django.http import JsonResponse


def api(request):
    id_type = request.GET.get('id_type')
    value = request.GET.get('value')

    c = Converter()

    results = {}
    if id_type == 'symbol':
        results, score = c.convert_symbol(value)
    elif id_type == 'name':
        results, score = c.convert_name(value)
    elif id_type == 'ensembl':
        results, score = c.convert_ensembl(value)
    elif id_type == 'entrez':
        results, score = c.convert_entrez(value)
    elif id_type == 'alias':
        results, score = c.convert_symbol(value)
    else:
        results, score = {'error': 'invalid input'}, 0

    return JsonResponse({'id_type': id_type, 'value': value, 'score': score, 'results_count': len(results), 'results': results })
