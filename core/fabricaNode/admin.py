from django.contrib import admin

from core.fabricaNode.models import (
    Area,
    Autor,
    Cidade,
    Editora,
    Estado,
    Keyword,
    Pais,
    Publicacao,
    Subarea,
)

admin.site.register(Autor)
admin.site.register(Cidade)
admin.site.register(Editora)
admin.site.register(Estado)
admin.site.register(Pais)
admin.site.register(Publicacao)
admin.site.register(Keyword)
admin.site.register(Area)
admin.site.register(Subarea)
