from django.db import models


class GeneInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    gene_name = models.TextField()
    symbol = models.TextField()
    class Meta:
    	db_table = 'gene_info'

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