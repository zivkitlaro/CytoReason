from django.contrib import admin

from .models import Alias
from .models import GeneInfo


class GeneInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'gene_name', 'symbol']


admin.site.register(GeneInfo, GeneInfoAdmin)


class AliasAdmin(admin.ModelAdmin):
    list_display = ['id', 'gene', 'alias_symbol']


admin.site.register(Alias, AliasAdmin)
