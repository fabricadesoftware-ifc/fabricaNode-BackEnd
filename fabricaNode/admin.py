from django.contrib import admin

from .models import Autor, Cidade, Editora, Estado, Pais, Publicacao, Keyword, Publicacao_keyword, Area, Subarea

admin.site.register(Autor)
admin.site.register(Cidade)
admin.site.register(Editora)
admin.site.register(Estado)
admin.site.register(Pais)
admin.site.register(Publicacao)
admin.site.register(Keyword)
admin.site.register(Publicacao_keyword)
admin.site.register(Area)
admin.site.register(Subarea)