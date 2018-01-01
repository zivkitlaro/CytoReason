from django.db import models
from django.core.urlresolvers import reverse

def convert(id_type, value):
	return 'sure, yeah'

#from GeneMapperApp.models import GeneInfo, Entres, Alias, Converter
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

	def convert_symbol(self, value):
		return 'symbol:' + value

	def convert_name(self, value):
		return 'name:' + value

	def convert_alias(self, value):
		return 'alias:' + value

	def convert_entrez(self, value):
		return 'entrez:' + value

	def convert_ensembl(self, value):
		return 'ensembl:' + value



class GeneInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    gene_name = models.TextField()
    symbol = models.TextField()
    class Meta:
    	db_table = 'gene_info'

    def get_absolute_url(self):
    	return reverse('GeneMapperApp:geneinfo_detail', args=[self.id])

class Entres(models.Model):
	id = models.IntegerField(primary_key=True)
	gene = models.ForeignKey(GeneInfo, related_name='entrez', primary_key=True)
	entrez_id = models.TextField()
	class Meta:
		db_table = 'genes'

class Alias(models.Model):
	id = models.IntegerField(primary_key=True)
	alias_symbol = models.TextField()
	gene = models.ForeignKey(GeneInfo, related_name='aliases')

	class Meta:
		db_table = 'alias'