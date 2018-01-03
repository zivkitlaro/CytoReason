from django.db import models
import json


# from genemapper.models import GeneInfo, Entrez, Alias, Ensembl, Converter
# g = GeneInfo.objects.first()
# c = Converter()
# c.find_genes_from_symbol('A1BG', False)

class Converter():
    def convert(self, value_type, value):
        if value_type == 'symbol':
            return self.convert_symbol(value)
        elif value_type == 'name':
            return self.convert_name(value)
        elif value_type == 'alias':
            return self.convert_alias(value)
        elif value_type == 'ensembl':
            return self.convert_ensembl(value)
        elif value_type == 'entrez':
            return self.convert_entrez(value)

        return 'nope'

    def find_genes_from_symbol(self, value: str, searchContained: bool) -> object:
        candidates = list()

        if searchContained:
            genes = GeneInfo.objects.filter(symbol__icontains=value)
        else:
            genes = GeneInfo.objects.filter(symbol=value)

        for gene in genes:
            candidates.append(gene)

        if searchContained:
            aliases = Alias.objects.filter(alias_symbol__icontains=value)
        else:
            aliases = Alias.objects.filter(alias_symbol=value)

        gene_ids_from_aliases = list(
            aliases.values_list('gene_id', flat=True).distinct())

        existingIds = genes.values_list('id', flat=True)
        for existingId in existingIds:
            gene_ids_from_aliases.remove(existingId)

        genes_from_aliases = GeneInfo.objects.filter(id__in=gene_ids_from_aliases)

        for gene in genes_from_aliases:
            if gene not in candidates:
                candidates.append(gene)

        if len(candidates) == 0 and searchContained is False:
            return self.find_genes_from_symbol(value, True)

        score = 100.0/len(candidates)

        return candidates, score

    def convert_symbol(self, value):

        dictionaries = list()
        genes, score = self.find_genes_from_symbol(value, False)
        for gene in genes:
            dictionaries.append(gene.dictionary)

        print('input symbol:' + value)
        print('score: ' + str(score))
        print('result: ' + json.dumps(dictionaries))

        return total, score

    def convert_name(self, value):

        dictionaries = list()
        genes = GeneInfo.objects.filter(gene_name__icontains=value)

        for gene in genes:
            dictionaries.append(gene.dictionary)

        if len(genes) == 0:
            return dictionaries, 0

        score = 100 / len(genes)

        print('input name:' + value)
        print('score: ' + str(score))
        print('result: ' + json.dumps(dictionaries))

        return dictionaries, score

    def convert_alias(self, value):
        return 'alias:' + value

    def convert_entrez(self, value):

        entrezes = Entrez.objects.filter(entrez_id=value)
        genes = list()
        dictionaries = list()
        for entrez in entrezes:
            if entrez.gene not in genes:
                genes.append(entrez.gene)
                dictionaries.append(entrez.gene.dictionary)

        if len(genes) == 0:
            return dictionaries, 0

        score = 100 / len(genes)

        print('input entrez:' + value)
        print('score: ' + str(score))
        print('result: ' + json.dumps(dictionaries))

        return dictionaries, score

    def convert_ensembl(self, value):
        return 'ensembl:' + value


class GeneInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    gene_name = models.TextField()
    symbol = models.TextField()

    class Meta:
        db_table = 'gene_info'

    @property
    def str(self):
        return 'Gene(' + str(self.id) + '): ' + self.gene_name + ', ' + str(self.aliases_symbols)

    @property
    def entrezId(self):
        entrez = self.entrez.all()
        if len(entrez) > 1:
            assert 'should be only 1'
        return entrez.first().entrez_id

    @property
    def ensemblId(self):
        ensembl = self.ensembl.all()
        if len(ensembl) == 0:
            return '-'

        if len(ensembl) > 1:
            assert 'should be only 1'
        return ensembl.first().ensembl_id

    @property
    def aliases_symbols(self):
        aliases = list(self.aliases.all().values_list('alias_symbol', flat=True))
        aliases.remove(self.symbol)
        return aliases

    def __str__(self):
        return self.str

    # def get_absolute_url(self):
    # 	return reverse('GeneMapperApp:geneinfo_detail', args=[self.id])

    @property
    def dictionary(self):
        return {'gene_id': self.id, 'name': self.gene_name, 'symbol': self.symbol, 'aliases': self.aliases_symbols,
                      'entrez_id': self.entrezId, 'ensembl_id': self.ensemblId}

class Entrez(models.Model):
    id = models.IntegerField(primary_key=True)
    gene = models.ForeignKey(GeneInfo, related_name='entrez', primary_key=True, on_delete=models.CASCADE)
    entrez_id = models.TextField()

    class Meta:
        db_table = 'genes'


class Alias(models.Model):
    id = models.IntegerField(primary_key=True)
    alias_symbol = models.TextField()
    gene = models.ForeignKey(GeneInfo, related_name='aliases', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'alias'


class Ensembl(models.Model):
    id = models.IntegerField(primary_key=True)
    gene = models.ForeignKey(GeneInfo, related_name='ensembl', primary_key=True, on_delete=models.CASCADE)
    ensembl_id = models.TextField()

    class Meta:
        db_table = 'ensembl'
