"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from fabricaNode.views import AreaViewSet, AutorViewSet, CidadeViewSet, EditoraViewSet, EstadoViewSet, KeywordViewSet, PaisViewSet, Publicacao_keywordViewSet, PublicacaoViewSet, SubareaViewSet

router = DefaultRouter()

router.register(r'areas', AreaViewSet)
router.register(r'autors', AutorViewSet)
router.register(r'cidades', CidadeViewSet)
router.register(r'editoras', EditoraViewSet)
router.register(r'estados', EstadoViewSet)
router.register(r'keywords', KeywordViewSet)
router.register(r'pais', PaisViewSet)
router.register(r'publicacao_keywords', Publicacao_keywordViewSet)
router.register(r'publicacaos', PublicacaoViewSet)
router.register(r'subareas', SubareaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
]
