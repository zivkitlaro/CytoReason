from django.shortcuts import render, get_object_or_404
from .models import GeneInfo, Alias

def geneinfo_list(request):
	geneinfos = GeneInfo.all()
	return render(request, 'GeneMapperApp/geneinfo/list.html', {'GeneInfos': geneinfos})

def geneinfo_detail(id):
	geneinfo = get_object_or_404(GeneInfo, id=id)
	return render(request, 'GeneMapperApp/geneinfo/detail.html', {'geneinfo': geneinfo})
