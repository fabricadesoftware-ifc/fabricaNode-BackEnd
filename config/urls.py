from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from core.fabricaNode.views import (AreaViewSet, AutorViewSet, CidadeViewSet,
                                    EditoraViewSet, EstadoViewSet,
                                    KeywordViewSet, PaisViewSet,
                                    PublicacaoViewSet, SubareaViewSet)
from core.usuario.router import router as usuario_router

router = DefaultRouter()

router.register(r"areas", AreaViewSet)
router.register(r"autores", AutorViewSet)
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
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
