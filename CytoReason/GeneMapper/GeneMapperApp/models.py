from django.db import models

class GeneInfo(models.Model):
    _id = models.IntegerField(primary_key=True)
    gene_name = models.TextField()
    symbol = models.TextField()

    class Meta:
		db_table = 'gene_info'


