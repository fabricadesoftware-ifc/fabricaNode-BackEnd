from django.contrib import admin

from .models import autor, cidade, editora, estado, pais, publicacao, keyword, publicacao_keyword

admin.site.register(autor)
admin.site.register(cidade)
admin.site.register(editora)
admin.site.register(estado)
admin.site.register(pais)
admin.site.register(publicacao)
admin.site.register(keyword)
admin.site.register(publicacao_keyword)
