from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from core.fabricaNode.views import (AreaViewSet, AutorViewSet, CidadeViewSet,
                                    EditoraViewSet, EstadoViewSet,
                                    KeywordViewSet, OpenAlexBuscarView,
                                    OpenAlexConfirmarView, OpenAlexObrasView,
                                    OrcidBuscarView, OrcidConfirmarView,
                                    OrcidObrasView, PaisViewSet,
                                    PublicacaoViewSet, SubareaViewSet)
from core.usuario.router import router as usuario_router

router = DefaultRouter()

router.register(r"areas", AreaViewSet)
router.register(r"autors", AutorViewSet)
router.register(r"cidades", CidadeViewSet)
router.register(r"editoras", EditoraViewSet)
router.register(r"estados", EstadoViewSet)
router.register(r"keywords", KeywordViewSet)
router.register(r"pais", PaisViewSet)
router.register(r"publicacaos", PublicacaoViewSet)
router.register(r"subareas", SubareaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/", include(usuario_router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/orcid/buscar/", OrcidBuscarView.as_view(), name="orcid-buscar"),
    path(
        "api/orcid/obras/<str:orcid_id>/",
        OrcidObrasView.as_view(),
        name="orcid-obras",
    ),
    path(
        "api/orcid/confirmar/", OrcidConfirmarView.as_view(), name="orcid-confirmar"
    ),
    path(
        "api/openalex/buscar/", OpenAlexBuscarView.as_view(), name="openalex-buscar"
    ),
    path(
        "api/openalex/obras/<str:openalex_id>/",
        OpenAlexObrasView.as_view(),
        name="openalex-obras",
    ),
    path(
        "api/openalex/confirmar/",
        OpenAlexConfirmarView.as_view(),
        name="openalex-confirmar",
    ),
]
