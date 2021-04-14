from django.contrib.gis.db import models


class MunicipiosIBGE(models.Model):
    ibge_id = models.CharField(max_length=7)
    nome = models.CharField(max_length=60)
    sigla_uf = models.CharField(max_length=2)
    area_km2 = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
